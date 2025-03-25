import os
import httpx
import tempfile



def solver_1(command: str):
    return '''Version:          Code 1.96.2 (fabdb6a30b49f79a7aba0f2ad9df9b399473380f, 2024-12-19T10:22:47.216Z)
OS Version:       Darwin arm64 24.2.0
CPUs:             Apple M1 (8 x 2400)
Memory (System):  8.00GB (0.09GB free)
Load (avg):       2, 6, 6
VM:               0%
Screen Reader:    no
Process Argv:     --crash-reporter-id ca90dba9-1235-4414-b9a6-6a7e9b4e613b
GPU Status:       2d_canvas:                              enabled
                  canvas_oop_rasterization:               enabled_on
                  direct_rendering_display_compositor:    disabled_off_ok
                  gpu_compositing:                        enabled
                  multiple_raster_threads:                enabled_on
                  opengl:                                 enabled_on
                  rasterization:                          enabled
                  raw_draw:                               disabled_off_ok
                  skia_graphite:                          disabled_off
                  video_decode:                           enabled
                  video_encode:                           enabled
                  webgl:                                  enabled
                  webgl2:                                 enabled
                  webgpu:                                 enabled
                  webnn:                                  disabled_off

CPU %	Mem MB	   PID	Process
    0	   115	  1439	code main
    0	    49	  1443	   gpu-process
    0	    16	  1444	   utility-network-service
    0	   188	  1445	window [1] (Welcome)
    0	    33	  1485	shared-process
    0	    16	  1486	fileWatcher [1]
    0	    25	  1487	extensionHost [1]
    0	    25	  1547	ptyHost
    0	     0	  1548	     /bin/zsh -il
    0	     0	  1675	     /bin/bash --init-file /Applications/Visual Studio Code.app/Contents/Resources/app/out/vs/workbench/contrib/terminal/common/scripts/shellIntegration-bash.sh'''


def solver_2(url: str, param: str, value: str):
    import subprocess
    import json

    # Run the command using uv run with httpie
    cmd = ["uv", "run", "--with", "httpie", "--", "https", f"{url}", f"{param}=={value}"]
    result = subprocess.run(cmd, capture_output=True, text=True)

    # Print the JSON output
    return f'''{json.dumps(json.loads(result.stdout), indent=2)}'''


def solver_3(req_filename: str, temp_dir: str, file_path: str, file_name: str, command: str):
    import subprocess
    import json
    import os

    os.chdir(f"{temp_dir}")

    # pre_cmd = ["mv", f"{file_name}", f"{req_filename}"]
    # pre_cmd = ["pwd"]
    # print(subprocess.run(pre_cmd, capture_output=True, text=True))

    
    # Run the command in the directory with the downloaded file
    cmd = [f"{command}"]
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)

    # Print the output of the command
    return f'''{result.stdout[:-4]}'''

def solver_4(formula: str):
    import os
    import httpx
    import tempfile
    import subprocess
    try:
        api_key = os.getenv('AIPROXY_TOKEN')
        response = httpx.post("http://aiproxy.sanand.workers.dev/openai/v1/chat/completions",
                            headers={
                                "Authorization": f"Bearer {api_key}",
                                    "Content-Type": "application/json",
                                
                            }, 
                            json={
                                "model": "gpt-4o-mini",
                                    "messages": [
                
                {"role": "system", "content": "You are given a Google Sheets formula. Generate a code only in python using only built-in libraries that will achieve the same result such that it prints only the answer of the formula. Give the code only without any markdown in plain text but maintain indentation"},
                {"role": "user", "content": f"{formula}"},
            ]
        })

        python_script = response.json()["choices"][0]["message"]["content"]
        print(python_script)
        temp_dir = tempfile.mkdtemp()
        with open(f"{temp_dir}/temp_script.py", 'w') as temp_script:
            temp_script.write(str(python_script))

        os.chmod(f"{temp_dir}/temp_script.py", 0o755)


        result = subprocess.run(["python3", f"{temp_dir}/temp_script.py"], capture_output=True, text=True)
        os.remove(f"{temp_dir}/temp_script.py")
        os.removedirs(temp_dir)
        return result.stdout[:-1]
    
    except Exception as e:
        return {"message": "task execution failed", "status_code": 500}
    
def solver_5(formula: str):
    import os
    import httpx
    import tempfile
    import subprocess
    try:
        api_key = os.getenv('AIPROXY_TOKEN')
        response = httpx.post("http://aiproxy.sanand.workers.dev/openai/v1/chat/completions",
                            headers={
                                "Authorization": f"Bearer {api_key}",
                                    "Content-Type": "application/json",
                                
                            }, 
                            json={
                                "model": "gpt-4o-mini",
                                    "messages": [
                
                {"role": "system", "content": "You are given a Microsoft Excel formula. Generate a code only in python using only built-in libraries that will achieve the same result such that it prints only the answer of the excel formula. Give the code only without any markdown in plain text but maintain indentation"},
                {"role": "user", "content": f"{formula}"},
            ]
        })

        python_script = response.json()["choices"][0]["message"]["content"]
        print(python_script)
        temp_dir = tempfile.mkdtemp()
        with open(f"{temp_dir}/temp_script.py", 'w') as temp_script:
            temp_script.write(str(python_script))

        os.chmod(f"{temp_dir}/temp_script.py", 0o755)


        result = subprocess.run(["python3", f"{temp_dir}/temp_script.py"], capture_output=True, text=True)
        os.remove(f"{temp_dir}/temp_script.py")
        os.removedirs(temp_dir)
        return result.stdout[:-1]
    
    except Exception as e:
        return {"message": "task execution failed", "status_code": 500}
    
def solver_6(html_element: str):
    try:
        api_key = os.getenv('AIPROXY_TOKEN')
        response = httpx.post("http://aiproxy.sanand.workers.dev/openai/v1/chat/completions",
                            headers={
                                "Authorization": f"Bearer {api_key}",
                                    "Content-Type": "application/json",
                                
                            }, 
                            json={
                                "model": "gpt-4o-mini",
                                    "messages": [
                
                {"role": "system", "content": "You are given an HTML element. Return the value of the hidden input in the HTML element. Only the value nothing else in plain text."},
                {"role": "user", "content": f"{html_element}"},
            ]
        })
        hidden_value = response.json()["choices"][0]["message"]["content"]
        return hidden_value
    except Exception as e:
        return {"message": "task execution failed", "status_code": 500}



def solver_7(day_name: str, start_date: str, end_date: str):
    import datetime
    start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d")
    end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d")
    day_count = 0
    for i in range((end_date - start_date).days + 1):
        day = start_date + datetime.timedelta(days=i)
        if day.strftime("%A") == day_name:
            day_count += 1
    return f'''{day_count}'''


def solver_8(temp_dir: str, file_path: str, file_name: str, csv_file: str, column_name: str):
    # Unzip the file
    import zipfile
    import csv
    with zipfile.ZipFile(file_path, 'r') as zip_ref:
        zip_ref.extractall(temp_dir)

    # Read the CSV file

    csv_file_path = os.path.join(temp_dir, csv_file)
    with open(csv_file_path, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            if column_name in row:
                return row[column_name]
        return f"Column {column_name} not found in the CSV file."


def solver_9(json_array: list, first_field: str, second_field: str):
    import json
    json_array = json.loads(json_array)
    for i in range(len(json_array)):
        for j in range(len(json_array)):
            if(json_array[j][first_field] > json_array[i][first_field]):
                json_array[i], json_array[j] = json_array[j], json_array[i]
            elif(json_array[j][first_field] == json_array[i][first_field]):
                if(json_array[j][second_field] > json_array[i][second_field]):
                    json_array[i], json_array[j] = json_array[j], json_array[i]
    
    return f'''{json.dumps(json_array, separators=(',', ':'))}'''

def solver_10(temp_dir: str, file_path: str, file_name: str):
    import json
    import hashlib
    import subprocess
    import shlex
    # Dictionary to store key-value pairs
    key_value_pairs = {}
    
    # Read the file and parse each line
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if '=' in line:
                key, value = line.split('=', 1)
                key_value_pairs[key] = value
    json_string = json.dumps(key_value_pairs)

    # Escape the JSON string for command line
    escaped_json = shlex.quote(json_string)

    # Command to run the Node.js script with the JSON argument
    command = f"node ./js-utils/hash.js {escaped_json}"

    # Run the command
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Get the output
    stdout, stderr = process.communicate()

    # Print the output
    return f'''{stdout.decode('utf-8').strip()}'''


def solver_11(html_element: str, given_class: str, given_attribute: str, hidden_html: str):
    from bs4 import BeautifulSoup

    # Parse the HTML
    soup = BeautifulSoup(hidden_html, 'html.parser')

    # Find all <div> elements with class 'foo'
    foo_divs = soup.find_all(html_element, class_=given_class)

    # Extract their data-value attributes and convert to integers
    data_values = [int(div[given_attribute]) for div in foo_divs]

    # Calculate the sum of the data-value attributes
    sum_data_values = sum(data_values)

    return f'''{sum_data_values}'''


def solver_12(temp_dir: str, file_path: str, file_name: str, file_1: str, encoding_1: str, file_2: str, encoding_2: str, file_3: str, encoding_3: str, symbol_1: str, symbol_2: str, symbol_3: str):
    import zipfile
    import csv
    with zipfile.ZipFile(file_path, 'r') as zip_ref:
        zip_ref.extractall(temp_dir)
    
    file_1_path = os.path.join(temp_dir, file_1)
    file_2_path = os.path.join(temp_dir, file_2)
    file_3_path = os.path.join(temp_dir, file_3)

    encodings = [encoding_1, encoding_2, encoding_3]
    for i in range(len(encodings)):
        if encodings[i] == 'CP-1252':
            encodings[i] = 'cp1252'
        elif encodings[i] == 'UTF-8':
            encodings[i] = 'utf-8'
        elif encodings[i] == 'UTF-16':
            encodings[i] = 'utf-16'
    
    import pandas as pd
    df = pd.read_csv(file_1_path, encoding=encodings[0])
    filtered_df = df[(df.symbol == symbol_1) | (df.symbol == symbol_2) | (df.symbol == symbol_3) ]

    sum_1 = filtered_df['value'].sum()

    df_2 = pd.read_csv(file_2_path, encoding=encodings[1])
    filtered_df_2 = df_2[(df_2.symbol == symbol_1) | (df_2.symbol == symbol_2) | (df_2.symbol == symbol_3) ]

    sum_2 = filtered_df_2['value'].sum()

    df_3 = pd.read_csv(file_3_path, encoding=encodings[2], sep='\t')
    filtered_df_3 = df_3[(df_3.symbol == symbol_1) | (df_3.symbol == symbol_2) | (df_3.symbol == symbol_3) ]

    sum_3 = filtered_df_3['value'].sum()

    return f'''{sum_1 + sum_2 + sum_3}'''

def solver_13(file_name: str, value: str):
    import tempfile
    import os
    import subprocess

    temp_dir = tempfile.mkdtemp()
    repo_url = "https://github.com/pradeepmondal/tds-solver-playground.git"
    repo_dir = os.path.join(temp_dir, "repo")

    # Clone the repository
    subprocess.run(["git", "clone", repo_url, repo_dir], check=True)

    # Change to the repository directory
    os.chdir(repo_dir)

    # Create the file with the given value
    with open(file_name, 'w') as file:
        file.write(value)

    # Add the file to the repository
    subprocess.run(["git", "add", file_name], check=True)

    # Commit the changes
    subprocess.run(["git", "commit", "-m", "Add new file with given value"], check=True)

    # Push the changes
    subprocess.run(["git", "push"], check=True)

    return f"https://raw.githubusercontent.com/pradeepmondal/tds-solver-playground/refs/heads/main/{file_name}"

def solver_14(temp_dir: str, file_path: str, file_name: str, existing_word: str, new_word: str, command: str):
    import tempfile
    import os
    import subprocess
    import zipfile
    import shlex
    import re

    new_temp = tempfile.mkdtemp()
    with zipfile.ZipFile(file_path, 'r') as zip_ref:
        zip_ref.extractall(new_temp)

    def replace_in_all_files(directory, old_word, new_word):
    # Compile the regex pattern for case-insensitive search
        pattern = re.compile(re.escape(old_word), re.IGNORECASE)
        
        # Count for reporting
        files_modified = 0
        replacements_made = 0
        
        # Walk through all files in the directory
        for root, _, files in os.walk(directory):
            for filename in files:
                file_path = os.path.join(root, filename)
                
                # Skip non-text files (optional)
                try:
                    # Try to open and read the file
                    with open(file_path, 'r', encoding='utf-8') as file:
                        content = file.read()
                    
                    # Count original occurrences
                    original_count = len(pattern.findall(content))
                    
                    if original_count > 0:
                        # Perform the replacement
                        new_content = pattern.sub(new_word, content)
                        
                        # Write the modified content back to the file
                        with open(file_path, 'w', encoding='utf-8') as file:
                            file.write(new_content)
                        
                        files_modified += 1
                        replacements_made += original_count
                        print(f"Modified {file_path}: {original_count} replacements")
                        
                except (UnicodeDecodeError, IOError):
                    # Skip files that can't be read as text
                    print(f"Skipped {file_path}: not a text file or cannot be read")
                    continue
        
        print(f"\nSummary: Modified {files_modified} files with {replacements_made} total replacements")
    
    replace_in_all_files(new_temp, existing_word, new_word)

    # Run the provided command in the temp_dir
    os.chdir(new_temp)
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Get the output
    stdout, stderr = process.communicate()

    # Print the output
    return f'''{stdout.decode('utf-8').strip()[:-3]}'''


def solver_15(temp_dir: str, file_path: str, file_name: str, file_size_number: str, date_string: str):
    import os
    from datetime import datetime
    import pytz
    import zipfile
    import tempfile

    new_temp = tempfile.mkdtemp()
    def extract_with_timestamps(zip_filename, extract_dir='.'):
        with zipfile.ZipFile(zip_filename, 'r') as zip_ref:
            zip_ref.extractall(extract_dir)
            
            # After extraction, restore the original timestamps
            for info in zip_ref.infolist():
                if not info.is_dir():  # Skip directories initially
                    # Convert ZIP datetime tuple to timestamp
                    date_time = info.date_time
                    timestamp = datetime(*date_time).timestamp()
                    
                    # Set the timestamps for the extracted file
                    extracted_path = os.path.join(extract_dir, info.filename)
                    os.utime(extracted_path, (timestamp, timestamp))
            
            # Handle directories after files to avoid timestamp reset
            # when files are created inside directories
            for info in zip_ref.infolist():
                if info.is_dir():
                    date_time = info.date_time
                    timestamp = datetime.datetime(*date_time).timestamp()
                    
                    extracted_path = os.path.join(extract_dir, info.filename)
                    if os.path.exists(extracted_path):  # Directory might not exist if it was empty
                        os.utime(extracted_path, (timestamp, timestamp))
                    
    extract_with_timestamps(file_path, new_temp)

# Usage


    def calculate_filtered_files_size(directory='.', min_size_str='463', target_date_str='Sun, 31 Jan, 2010, 3:21 pm IST'):
        """
        Calculate the total size of files that meet specific criteria.
        
        Args:
            directory (str): Directory to search in (default: current directory)
            min_size_str (str): Minimum file size in bytes as a string (default: '463')
            target_date_str (str): Files modified on or after this date as a string 
                                in format "Sun, 31 Jan, 2010, 3:21 pm IST" (default: 'Sun, 31 Jan, 2010, 3:21 pm IST')
        
        Returns:
            tuple: (total_size, matching_files)
                - total_size (int): Total size in bytes of matching files
                - matching_files (list): List of tuples (file_path, size, modification_time)
        """
        # Convert min_size to integer
        min_size = int(min_size_str)
        
        # Parse the target date string
        target_date = datetime.strptime(target_date_str, "%a, %d %b, %Y, %I:%M %p IST")
        target_date = pytz.timezone('Asia/Kolkata').localize(target_date)
        
        # Convert target date to epoch time for comparison
        target_timestamp = target_date.timestamp()
        
        total_size = 0
        matching_files = []
        
        # Walk through all files in the specified directory
        for root, dirs, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                
                # Skip if not a file
                if not os.path.isfile(file_path):
                    continue
                    
                # Get file stats
                stats = os.stat(file_path)
                file_size = stats.st_size
                mod_time = stats.st_mtime
                
                # Check if file meets criteria
                if file_size >= min_size and mod_time >= target_timestamp:
                    total_size += file_size
                    matching_files.append((file_path, file_size, 
                                        datetime.fromtimestamp(mod_time, pytz.timezone('Asia/Kolkata'))))
        
        return total_size
    
    total_size = calculate_filtered_files_size(new_temp, file_size_number, date_string)
    return f'''{total_size}'''

def solver_16(temp_dir: str, file_path: str, file_name: str, command: str):
    import os
    import re
    import subprocess
    import shlex
    import tempfile
    import zipfile

    new_temp = tempfile.mkdtemp()
    with zipfile.ZipFile(file_path, 'r') as zip_ref:
        zip_ref.extractall(new_temp)

    def move_files_to_final(directory):
        final_dir = os.path.join(directory, "final")
        os.makedirs(final_dir, exist_ok=True)
        
        for root, _, files in os.walk(directory):
            if root == final_dir:
                continue
            for filename in files:
                file_path = os.path.join(root, filename)
                if os.path.isfile(file_path):
                    new_path = os.path.join(final_dir, filename)
                    os.rename(file_path, new_path)
        return final_dir

    final_dir = move_files_to_final(new_temp)

    
    def rename_files(directory):
        # Define a mapping for digit replacement
        digit_map = str.maketrans("0123456789", "1234567890")
        
        # Walk through all files in the directory
        for root, _, files in os.walk(directory):
            for filename in files:
                # Construct the full path to the file
                file_path = os.path.join(root, filename)
                
                # Skip directories
                if not os.path.isfile(file_path):
                    continue
                
                # Replace digits in the filename
                new_filename = re.sub(r'\d', lambda m: m.group(0).translate(digit_map), filename)
                
                # Construct the new full path
                new_file_path = os.path.join(root, new_filename)
                
                # Rename the file
                os.rename(file_path, new_file_path)
    
    rename_files(final_dir)

    # Run the provided command in the temp_dir
    os.chdir(final_dir)
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Get the output
    stdout, stderr = process.communicate()

    # Print the output
    return f'''{stdout.decode('utf-8').strip()[:-3]}'''

def solver_17(temp_dir: str, file_path: str, file_name: str, file_1: str, file_2: str):
    import zipfile
    with zipfile.ZipFile(file_path, 'r') as zip_ref:
        zip_ref.extractall(temp_dir)
    
    file_1_path = os.path.join(temp_dir, file_1)
    file_2_path = os.path.join(temp_dir, file_2)

    with open(file_1_path, 'r') as f1, open(file_2_path, 'r') as f2:
        file_1_lines = f1.readlines()
        file_2_lines = f2.readlines()

    diff_count = sum(1 for line1, line2 in zip(file_1_lines, file_2_lines) if line1 != line2)

    return f'''{diff_count}'''

def solver_18(ticket_type: str):
    ticket_type = ticket_type.lower()
    return f'''SELECT SUM(units*price) FROM tickets WHERE TRIM(LOWER(type)) = '{ticket_type}';'''


def solver_19():
    return '''# Daily Walking Analysis
## day-wise walking analysis done once a week

*Total Steps:*

| Sl No. | Person | Steps |
|----------|----------|----------|
| 1   | Pradeep   | **18000** |
| 2   | Rakesh   | **16900** |

Calculate Avg Daily Steps - `daily_steps`
```python
daily_steps = weekly_steps/7
```
know more about me -

![Pradeep Mondal](https://avatars.githubusercontent.com/u/42373983?v=4)

* [GitHub](https://github.com/pradeepmondal)
* [LinkedIn](https://www.linkedin.com/in/impradeepmondal)

Apart from walking, I do: 
1. Coding
2. Video Editing

This is total steps
>Total Steps'''

def solver_20(temp_dir: str, file_path: str, file_name: str, quality: int = 10):
    from pathlib import Path
    from PIL import Image
    import subprocess
    import os
    import io
    import base64

    output_path = os.path.join(temp_dir, 'compressed.png')

    with Image.open(file_path) as img:
        img.save(output_path, 'PNG', quality=quality, optimize=True)
    
    with open(output_path, 'rb') as f:
        compressed_image = f.read()
        compressed_image_base64 = base64.b64encode(compressed_image).decode('utf-8')
    
    return f'''{compressed_image_base64}'''

def solver_21(email_id: str):
    import tempfile
    import os
    import subprocess

    temp_dir = tempfile.mkdtemp()
    repo_url = "https://github.com/pradeepmondal/tds-solver-playground.git"
    repo_dir = os.path.join(temp_dir, "repo")

    # Clone the repository
    subprocess.run(["git", "clone", repo_url, repo_dir], check=True)

    # Change to the repository directory
    os.chdir(repo_dir)

    value = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
    <title>TDS Project 2 Playground</title>

</head>
<body>
    <div class="container">
    <h1 class="center">Tools in <span style="color: red;">Data Science</span> </h1> 
    
    
    <p class="para-text">This page is created exclusively for TDS Project 2</p>

    Contact Me:<br/>
    <!--email_off-->{email_id}<!--/email_off-->

</div>
    
</body>
</html>'''

    # Create the file with the given value
    with open('index.html', 'w') as file:
        file.write(value)

    # Add the file to the repository
    subprocess.run(["git", "add", "index.html"], check=True)

    # Commit the changes
    subprocess.run(["git", "commit", "-m", "Added index.html"], check=True)

    # Push the changes
    subprocess.run(["git", "push"], check=True)

    return f"https://pradeepmondal.github.io/tds-solver-playground/"


def solver_22(email_id: str):
    import hashlib
    hash_code = hashlib.sha256(f"{email_id} 2025".encode()).hexdigest()[-5:]
    return f'''{hash_code}'''


def solver_23(temp_dir: str, file_path: str, file_name: str, lightness_threshold: float):
    import numpy as np
    from PIL import Image

    import colorsys

    # There is a mistake in the line below. Fix it
    image = Image.open(file_path)

    rgb = np.array(image) / 255.0
    lightness = np.apply_along_axis(lambda x: colorsys.rgb_to_hls(*x)[1], 2, rgb)
    light_pixels = np.sum(lightness > lightness_threshold)
    

    return f'''{light_pixels}'''


def solver_24(temp_dir: str, file_path: str, file_name: str):
    ### Have to implement this later
    return f'''https://tds-deploy-assignments.vercel.app/api'''



def solver_25(email: str):
    import tempfile
    import os
    import subprocess

    temp_dir = tempfile.mkdtemp()
    repo_url = "https://github.com/pradeepmondal/tds-solver-playground.git"
    repo_dir = os.path.join(temp_dir, "repo")

    # Clone the repository
    subprocess.run(["git", "clone", repo_url, repo_dir], check=True)

    # Change to the repository directory
    os.chdir(repo_dir)
    os.mkdir(".github")
    os.chdir(".github")
    os.mkdir("workflows")
    os.chdir("workflows")

    # Create the file with the given value
    with open('test.yaml', 'w') as file:
        workflow = f'''name: Test Action

on: push

jobs:
  test-action:
    runs-on: ubuntu-latest
    steps:
      - name: {email}
        run: echo "Hello, world!"'''
        file.write(workflow)


    # Add the file to the repository
    subprocess.run(["git", "add", "test.yaml"], check=True)

    # Commit the changes
    subprocess.run(["git", "commit", "-m", "Add test workflow"], check=True)

    # Push the changes
    subprocess.run(["git", "push"], check=True)

    return f'''https://github.com/pradeepmondal/tds-solver-playground'''
    


def solver_26(tag: str): #### Need to check later ####
    import tempfile
    import os
    import subprocess

    temp_dir = tempfile.mkdtemp()
    repo_url = "https://github.com/pradeepmondal/tds-solver-playground.git"
    repo_dir = os.path.join(temp_dir, "repo")

    subprocess.run(["git", "clone", repo_url, repo_dir], check=True)

    os.chdir(repo_dir)

    with open('Dockerfile', 'w') as file:
        dockerfile = f'''FROM python:3.9-slim


WORKDIR /app


COPY . /app


EXPOSE 8080


CMD ["python", "server.py"]'''
        file.write(dockerfile)
    
    subprocess.run(["podman", "machine", "start"], check=True)
    subprocess.run(["podman", "build", "-t", f"tds-solver-playground:{tag}", "."], check=True)
    subprocess.run(["podman", "push", f"tds-solver-playground:{tag}"], check=True)

    return f'''https://hub.docker.com/repository/docker/pradeepmondal/tds-solver-playground/general'''
    

def solver_27():
    pass

def solver_28():
    pass

def solver_29(meaningless_text: str, model_name: str):
    from string import Template
    str_temp = Template('''import httpx

    response = httpx.post("https://api.openai.com/v1/chat/completions",
                        headers={
                            "Authorization": f"Bearer hello_abc",
                                "Content-Type": "application/json",
                            
                        }, 
                        json={
                            "model": "$model_name",
                                "messages": [
            {"role": "system", "content": "Analyze the sentiment of the given text into GOOD, BAD or NEUTRAL"},
            {"role": "user", "content": "$meaningless_text"},
        ]
    })''')
    return str_temp.substitute(meaningless_text=meaningless_text, model_name=model_name)

def solver_30(user_message: str):
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
                        "content": f"""{user_message}"""
                    }
                    ],
            },
        )
        raw_res = response.json()
        
        return f'''{raw_res['usage']['prompt_tokens']}'''
    except Exception as e:
        return {"message": "task execution failed", "status_code": 500}
    

def solver_31(required_fields: list, additionalPropertiesBoolean: bool):
    from string import Template
    import json
    str_temp =Template('''
{
  "model": "gpt-4o-mini",
  "messages": [
    { "role": "system", "content": "Respond in JSON" },
    { "role": "user", "content": "Generate 10 random addresses in the US" }
  ],
  "response_format": {
    "type": "json_schema",
    "json_schema": {
      "name": "addresses",
      "strict": true,
      "schema": {
        "type": "object",
        "properties": {
          "addresses": {
            "type": "array",
            "items": $item_str
          }
        },
        "required": ["addresses"],
        "additionalProperties": $additionalProperties
      }
    }
  }
}''')
    req_item = []
    for field in required_fields:
        req_item.append(field['field_name'])
    properties = {}
    for field in required_fields:
        properties[field['field_name']] = {"type": field['field_type']}
    items = {
        "type": "object",
        "properties": properties,
        "required": req_item,
        "additionalProperties": False
    }
    item_str = f'''{json.dumps(items)}'''

    
    
    
    additionalProperties = ''
    if additionalPropertiesBoolean:
        additionalProperties = "true"
    else:
        additionalProperties = "false"

    return f'''{str_temp.substitute(item_str=item_str, additionalProperties=additionalProperties)}'''
    

    
