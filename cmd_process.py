import os
import signal
import subprocess
import time
from subprocess import Popen

from pydantic.main import BaseModel


def file_name(job: str):
    return "result/" + "".join(job.split()) + ".txt"


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
        with open(file_name(job), "w") as outfile:
            self.command = subprocess.Popen(job.split(" "), preexec_fn=os.setsid, stdout=outfile)
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
