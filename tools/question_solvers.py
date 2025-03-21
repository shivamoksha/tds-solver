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



