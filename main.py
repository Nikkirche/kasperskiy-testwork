import os

from fastapi import FastAPI, HTTPException
from pathlib import Path
import subprocess

from cmd_process import Cmd_process

app = FastAPI(docs_url="/api/docs", redoc_url=None)
is_running:bool = False
process  = Cmd_process()


@app.post("/api/phoronix-perf")
async def actions_with_phoronix_perf_process(option: str):
    job = "phoronix-test-suite batch-run  compress-7zip"
    global process
    if option == "start":
        if is_running:
            raise HTTPException(status_code=400, detail="Job is already running!")
        process.start(job)
    elif option == "stop":
        if  not process.isRunning:
            raise HTTPException(status_code=400, detail="Job is not running!")
        process.stop()
    else:
        raise HTTPException(status_code=400, detail="Invalid option is given")


@app.get("api/phoronix-perf")
async def status_phoronix_perf_process():
    global process
    return process.stat()


@app.get("/api/phoronix-perf/result")
async def result_phoronix_perf_process():
    global process
    return

