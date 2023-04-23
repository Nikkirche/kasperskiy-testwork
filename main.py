import os
from typing import Final

from fastapi import FastAPI, HTTPException
from pathlib import Path
import subprocess

from cmd_process import Cmd_process

app = FastAPI(docs_url="/api/docs", redoc_url=None)
process = Cmd_process()
job: Final[str] = "7z b 3"


@app.post("/api/7z")
async def actions_with_7z(option: str):
    global process
    global job
    if option == "start":
        if process.isRunning:
            raise HTTPException(status_code=400, detail="Job is already running!")

        process.start(job)
    elif option == "stop":
        if not process.isRunning:
            raise HTTPException(status_code=400, detail="Job is not running!")
        process.stop()
    else:
        raise HTTPException(status_code=400, detail="Invalid option is given")


@app.get("/api/7z")
async def status_7z():
    global process
    return process.stat()


@app.get("/api/7z/result")
async def result_7z_process():
    global process
    return
