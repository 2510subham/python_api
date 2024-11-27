from typing import Union

from fastapi import FastAPI
import subprocess
app = FastAPI()

@app.get("/ping")
def read_root():
    return {"ping": "pong"}

@app.get("/run-script")
def run_script():
    try:
        script_path = "/C/Users/gangs/Music/python-api/hello.sh>py.log"  
        bash_path = "C:/Program Files/Git/bin/bash.exe"
        result = subprocess.run(
            [bash_path, "-c", script_path], 
            check=True,   
            stdout=subprocess.PIPE, 
            stderr=subprocess.PIPE 
        )
        return {
            "status": "success",
            "message": "Script executed successfully",
            # "stderr": result.stderr.decode("utf-8"),
        }
    except subprocess.CalledProcessError as e:
        print(e)
        return {
                "status": "error",
                "message": "Script execution failed",
            },