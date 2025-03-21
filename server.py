import httpx
from fastapi import FastAPI, UploadFile, Form, File, Query, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import PlainTextResponse
from typing import Annotated, Dict, Optional, List, Any, Tuple
from sentence_transformers import SentenceTransformer
import tempfile
import os
from tools.question_templates import question_templates
from tools.question_solvers import *
from tools.solvers_descriptions import solvers_descriptions
import re
import numpy as np
import json


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model = SentenceTransformer('all-MiniLM-L6-v2')

question_embeddings = {}
for q_id, q_statement in question_templates.items():
    
    clean_template = re.sub(r'\{\w+\}', "X", q_statement)
    question_embeddings[q_id] = model.encode(clean_template)


def identify_question(problem_statement: str) -> Tuple[Optional[int], float]:
    # Replace numbers with X to focus on the structure of the question
    normalized_statement = re.sub(r'\b\d+(\.\d+)?\b', 'X', problem_statement)
    
    # Generate embedding for the input problem statement
    input_embedding = model.encode(normalized_statement)
    
    # Find the most similar question template
    max_similarity = -1
    best_match_id = None
    
    for q_id, q_embedding in question_embeddings.items():
        # Calculate cosine similarity
        similarity = np.dot(input_embedding, q_embedding) / (np.linalg.norm(input_embedding) * np.linalg.norm(q_embedding))
        
        if similarity > max_similarity:
            max_similarity = similarity
            best_match_id = q_id
    
    return best_match_id, max_similarity

def extract_parameters(matched_ques_id, question):
    tools = [solvers_descriptions[matched_ques_id]]
    print(tools)
    try:
        response = httpx.post(
            "http://aiproxy.sanand.workers.dev/openai/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {os.getenv('AIPROXY_TOKEN')}",
                "Content-Type": "application/json",
            },
            json={
                "model": "gpt-4o-mini",
                "messages": [
                    {
                        "role": "user", 
                        "content": f"""{question}"""
                    }
                    ],
                "tools": tools,
                "tool_choice": "auto",
            },
        )
        output = response.json()["choices"][0]["message"]
        res = {"name": output["tool_calls"][0]["function"]["name"] , "arguments": output["tool_calls"][0]["function"]["arguments"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")
   
    fn = eval(res["name"])
    arguments = json.loads(res["arguments"])

    return arguments



    




@app.post("/api")
async def api(question: Annotated[str, Form()], file: UploadFile | None = None):
    if file:
        temp_dir = tempfile.mkdtemp()
        file_path = os.path.join(temp_dir, file.filename)
        
        with open(file_path, "wb") as f:
            content = await file.read()
            f.write(content)
        
    matched_ques_id, similarity = identify_question(question)

    print(matched_ques_id, similarity)

    solver = eval(f"solver_{matched_ques_id}")
    params = extract_parameters(matched_ques_id, question)
    print(params)
    if file:
        params["file_path"] = file_path
        params["file_name"] = file.filename
        params["temp_dir"] = temp_dir
    answer = solver(**params)
    if file:
        os.remove(file_path)
    return {"answer": answer}




if __name__ == "__main__":
    import uvicorn
    uvicorn.run("server:app", host="127.0.0.1", port=8080, reload=True)