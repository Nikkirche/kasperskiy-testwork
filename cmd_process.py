import os
import signal
import subprocess
import time
from pathlib import Path
from subprocess import Popen

from pydantic.main import BaseModel


def file_name(job: str, otype: str):
    return "result/" + "".join(job.split()) + otype + ".txt"


class DetailsStat(BaseModel):
    time: str


class Stat(BaseModel):
    isRunning: bool
    details: DetailsStat | None = None


class Cmd_process:

    def __init__(self):
        self.command = None
        self.start_time = None
        self.isRunning = False

    def start(self, job: str):
        self.isRunning = True
        out = Path(file_name(job, "out"))
        err = Path(file_name(job, "err"))
        out.parent.mkdir(parents=True, exist_ok=True)
        with out.open("w") as outfile, err.open("w") as errfile:
            self.command = subprocess.Popen(job.split(" "), preexec_fn=os.setsid, stdout=outfile, stderr=errfile)
        self.start_time = time.time()

    def stop(self):
        os.killpg(os.getpgid(self.command.pid), signal.SIGTERM)

        self.command = None
        self.isRunning = False

    def stat(self):
        if self.isRunning:
            return Stat(isRunning=self.isRunning,
                        details=DetailsStat(time=str(time.time() - self.start_time) + " Seconds"))
        else:
            return Stat(isRunning=self.isRunning)
