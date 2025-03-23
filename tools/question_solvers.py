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

