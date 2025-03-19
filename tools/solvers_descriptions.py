solvers_descriptions = {
    1: {
        "type": "function",
        "function": {
            "name": "solver_1",
            "description": "Gives output of a specific command in VS code",
            "parameters": {
                "type": "object",
                "properties": {
                    "command": {
                        "type": "string",
                        "description": "the command whose output is required"
                    },
                    

                },
                "required": ["command"],
                "additionalProperties": False
            },
            "strict": True
        }
    },

    2: {
        "type": "function",
        "function": {
            "name": "solver_2",
            "description": "Sends a HTTPS request to {url} with the URL encoded parameter {param} set to {email}",
            "parameters": {
                "type": "object",
                "properties": {
                    "url": {
                        "type": "string",
                        "description": "the URL to send the request to"
                    },
                    "param": {
                        "type": "string",
                        "description": "the URL encoded parameter"
                    },
                    "value": {
                        "type": "string",
                        "description": "the value set to the parameter"
                    }
                    

                },
                "required": ["url", "param", "value"],
                "additionalProperties": False
            },
            "strict": True
        }
    },

    3: {
        "type": "function",
        "function": {
            "name": "solver_3",
            "description": "Download the attached file . In the directory where you downloaded it, make sure it is called {req_filename}, and run {command} . Use npx and prettier.",
            "parameters": {
                "type": "object",
                "properties": {
                    "req_filename": {
                        "type": "string",
                        "description": "the name that the file should be renamed to"
                    },
                    "command": {
                        "type": "string",
                        "description": "the command whose output is required"
                    },
                    

                },
                "required": ["req_filename", "command"],
                "additionalProperties": False
            },
            "strict": True
        }
    },
}