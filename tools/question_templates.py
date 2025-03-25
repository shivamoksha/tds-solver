question_templates = {
    1: '''Install and run Visual Studio Code. In your Terminal (or Command Prompt), type code -s and press Enter. Copy and paste the entire output below. What is the output of {command}?''',

    2: '''
Running uv run --with httpie -- https [URL] installs the Python package httpie and sends a HTTPS request to the URL.
Send a HTTPS request to {url} with the URL encoded parameter {param} set to {email}
What is the JSON output of the command? (Paste only the JSON body, not the headers)''',

    3: '''Let's make sure you know how to use npx and prettier.
Download the attached file . In the directory where you downloaded it, make sure it is called {req_filename}, and run {command}
What is the output of the command?''',
    
    4: '''
Let's make sure you can write formulas in Google Sheets. Type this formula into Google Sheets.
{formula}
What is the result?''',

    5: '''
    Let's make sure you can write formulas in Microsoft Excel. Type this formula into Microsoft Excel.
Note: This will ONLY work in Office 365.
{excel_formula}
What is the result?''',

    6: '''{html_element}
Just above this paragraph, there's a hidden input with a secret value.
What is the value in the hidden input?''',

    7: '''How many {day_name} are there in the date range {start_date} to {end_date}?
The dates are in the year-month-day format. Include both the start and end date in your count. You can do this using any tool (e.g. Excel, Python, JavaScript, manually).''',

    8: '''Download and unzip file  which has a single {csv_file} file inside.
What is the value in the {column_name} column of the CSV file?''',

    9: '''Let's make sure you know how to use JSON. Sort this JSON array of objects by the value of the {first_field} field. In case of a tie, sort by the {second_field} field. Paste the resulting JSON below without any spaces or newlines.
    {json_array}''',

    10: '''Download and use multi-cursors and convert it into a single JSON object, where key=value pairs are converted into {key: value, key: value, ...}.
What's the result when you paste the JSON at tools-in-data-science.pages.dev/jsonhash and click the Hash button?''',

    11: '''Let's make sure you know how to select elements using CSS selectors. Find all {html_element}'s having a {given_class} class in the hidden element below. What's the sum of their {given_attribute} attributes?
{hidden_html}
Sum of data-value attributes:''',

    12: '''Download and process the files in  which contains three files with different encodings:
{file_1}: CSV file encoded in {encoding_1}
{file_2}: CSV file encoded in {encoding_2}
{file_3}: Tab-separated file encoded in {encoding_3}
Each file has 2 columns: symbol and value. Sum up all the values where the symbol matches {symbol_1} OR {symbol_2} OR {symbol_3} across all three files.
What is the sum of all values associated with these symbols?''',

    13: '''Let's make sure you know how to use GitHub. Create a GitHub account if you don't have one. Create a new public repository. Commit a single JSON file called {file_name} with the value {value} and push it.
Enter the raw Github URL of email.json so we can verify it. (It might look like https://raw.githubusercontent.com/[GITHUB ID]/[REPO NAME]/main/email.json.)''',

    14: '''Download  and unzip it into a new folder, then replace all {existing_word} (in upper, lower, or mixed case) with {new_word} in all files. Leave everything as-is - don't change the line endings.
What does running {command} in that folder show in bash?''',

    15: '''Download  and extract it. Use ls with options to list all files in the folder along with their date and file size.
What's the total size of all files at least {file_size_number} bytes large and modified on or after {date_string}?''',

    16: '''Download  and extract it. Use mv to move all files under folders into an empty folder. Then rename all files replacing each digit with the next. 1 becomes 2, 9 becomes 0, a1b9c.txt becomes a2b0c.txt.
What does running {command} in bash on that folder show?''',

    17: '''Download  and extract it. It has 2 nearly identical files, {file_1} and {file_2}, with the same number of lines.
How many lines are different between {file_1} and {file_2}?''',

    18: '''There is a tickets table in a SQLite database that has columns type, units, and price. Each row is a customer bid for a concert ticket.
{ticket_table}
What is the total sales of all the items in the {ticket_type} ticket type? Write SQL to calculate it.''',

    19: '''Write documentation in Markdown for an **imaginary** analysis of the number of steps you walked each day for a week, comparing over time and with friends. The Markdown must include:
{markdown_requirements}
''',

    20: '''Download the image below and compress it losslessly to an image that is less than 1,500 bytes. By losslessly, we mean that every pixel in the new image should be identical to the original image.
Upload your losslessly compressed image (less than 1,500 bytes)''',

    21: '''Publish a page using GitHub Pages that showcases your work. Ensure that your email address {email_id} is in the page's HTML.
GitHub pages are served via CloudFlare which obfuscates emails. So, wrap your email address inside a:
<!--email_off-->{email_id}<!--/email_off-->
What is the GitHub Pages URL? It might look like: https://[USER].github.io/[REPO]/''',

    22: '''Let's make sure you can access Google Colab. Run this program on Google Colab, allowing all required access to your email ID: {email_id}.
{python_code}
What is the result? (It should be a 5-character string)''',

    23: '''Download this image. Create a new Google Colab notebook and run this code (after fixing a mistake in it) to calculate the number of pixels with a certain minimum brightness:
    {python_code}
    What is the result? (It should be a number)''',

    24: '''Download this  which has the marks of 100 imaginary students.
Create and deploy a Python app to Vercel. Expose an API so that when a request like https://your-app.vercel.app/api?name=X&name=Y is made, it returns a JSON response with the marks of the names X and Y in the same order, like this:
{ "marks": [10, 20] }
Make sure you enable CORS to allow GET requests from any origin.
What is the Vercel URL? It should look like: https://your-app.vercel.app/api''',

    25: '''Create a GitHub action on one of your GitHub repositories. Make sure one of the steps in the action has a name that contains your email address {email}. For example:
jobs:
  test:
    steps:
      - name: {email}
        run: echo "Hello, world!"
Trigger the action and make sure it is the most recent action.
What is your repository URL? It will look like: https://github.com/USER/REPO''',

    26: '''Create and push an image to Docker Hub. Add a tag named {tag} to the image.
What is the Docker image URL? It should look like: https://hub.docker.com/repository/docker/$USER/$REPO/general''',

    27: '''empty_question''', #Do later
    28: '''empty_question''', #Do later

    29: '''One of the test cases involves sending a sample piece of meaningless text:
{meaningless_text}
Write a Python program that uses httpx to send a POST request to OpenAI's API to analyze the sentiment of this (meaningless) text into GOOD, BAD or NEUTRAL. Specifically:

Make sure you pass an Authorization header with dummy API key.
Use {model_name} as the model.
The first message must be a system message asking the LLM to analyze the sentiment of the text. Make sure you mention GOOD, BAD, or NEUTRAL as the categories.
The second message must be exactly the text contained above.
This test is crucial for DataSentinel Inc. as it validates both the API integration and the correctness of message formatting in a controlled environment. Once verified, the same mechanism will be used to process genuine customer feedback, ensuring that the sentiment analysis module reliably categorizes data as GOOD, BAD, or NEUTRAL. This reliability is essential for maintaining high operational standards and swift response times in real-world applications.

Note: This uses a dummy httpx library, not the real one. You can only use:

response = httpx.get(url, **kwargs)
response = httpx.post(url, json=None, **kwargs)
response.raise_for_status()
response.json()''',

    30: '''To optimize operational costs and prevent unexpected API overages, the engineering team at LexiSolve has developed an internal diagnostic tool that simulates and measures token usage for typical prompts sent to the language model.
One specific test case an understanding of text tokenization. Your task is to generate data for that test case.
Specifically, when you make a request to OpenAI's GPT-4o-Mini with just this user message:
{user_message}
... how many input tokens does it use up?''',

    31: '''As part of the integration process, you need to write the body of the request to an OpenAI chat completion call that:
Uses model gpt-4o-mini
Has a system message: Respond in JSON
Has a user message: Generate 10 random addresses in the US
Uses structured outputs to respond with an object addresses which is an array of objects with required fields: {required_fields} .
Sets additionalProperties to {additionalPropertiesBoolean} to prevent additional properties.
Note that you don't need to run the request or use an API key; your task is simply to write the correct JSON body.
What is the JSON body we should send to https://api.openai.com/v1/chat/completions for this? (No need to run it or to use an API key. Just write the body of the request below.)'''



}