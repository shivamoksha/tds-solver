import httpx
from fastapi import FastAPI, UploadFile, Form, File, Query, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import PlainTextResponse
from typing import Annotated
import tempfile
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/api")
async def api(question: Annotated[str, Form()], file: UploadFile = File(...)):
    
    
    with tempfile.TemporaryDirectory() as temp_dir:
        
        file_path = os.path.join(temp_dir, file.filename)
        
        with open(file_path, "wb") as f:
            content = await file.read()
            f.write(content)
    
    return {
            
            "answer": "dummy answer",
            
        }




if __name__ == "__main__":
    import uvicorn
    uvicorn.run("server:app", host="127.0.0.1", port=8080, reload=True)