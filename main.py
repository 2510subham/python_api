from typing import Union

from fastapi import FastAPI, Header, HTTPException

import subprocess
app = FastAPI()

@app.get("/ping")
def read_root():
    try:
        return {"ping": "pong"}
    except Exception as e:
        return {"error": str(e)}

@app.get("/run")
def run_script(authorization: str = Header("")):
    try:
        script_path = "/C/Users/gangs/Music/python-api/hello.sh>py.log"  
        bash_path = "C:/Program Files/Git/bin/bash.exe"
        # want to verify header also
        # authorization: str = Header(...)
        print("Script path: ", authorization)
        if authorization != "abcd1234":
            raise HTTPException(status_code=401, detail="Unauthorized")
        result = subprocess.run(
            [bash_path, "-c", script_path], 
            check=True,   
            stdout=subprocess.PIPE, 
            stderr=subprocess.PIPE 
        )
        return {
            "status": "success",
            "detail": "Script executed successfully",
            # "stderr": result.stderr.decode("utf-8"),
        }
    except subprocess.CalledProcessError as e:
        print(e)
        raise HTTPException(status_code=401,detail="Script Execution Failed")