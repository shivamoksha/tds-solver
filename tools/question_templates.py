question_templates = {
    1: '''Install and run Visual Studio Code. In your Terminal (or Command Prompt), type code -s and press Enter. Copy and paste the entire output below. What is the output of {command}?''',

    2: '''
Running uv run --with httpie -- https [URL] installs the Python package httpie and sends a HTTPS request to the URL.
Send a HTTPS request to {url} with the URL encoded parameter {param} set to {email}
What is the JSON output of the command? (Paste only the JSON body, not the headers)''',

    3: '''Let's make sure you know how to use npx and prettier.
Download the attached file . In the directory where you downloaded it, make sure it is called {req_filename}, and run {command}
What is the output of the command?'''
}