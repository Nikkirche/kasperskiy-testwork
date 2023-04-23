from typing import Final

from fastapi import FastAPI, HTTPException
from pathlib import Path

from .cmdprocess import CmdProcess
from .models import Result
from .utils import file_name

app = FastAPI(docs_url="/api/docs", redoc_url=None)
process = CmdProcess()
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
    return {"status": "Successful"}


@app.get("/api/7z")
async def status_7z():
    global process
    return process.stat()


@app.get("/api/7z/result")
async def result_7z_process():
    global process
    out_path = Path(file_name(job, "out"))
    err_path = Path(file_name(job, "err"))
    if not (out_path.exists() or err_path.exists()):
        raise HTTPException(status_code=404, detail="No results")
    out = out_path.read_text()if out_path.exists() else None
    err = err_path.read_text()if err_path.exists() else None
    return Result(output=out, err=err)
