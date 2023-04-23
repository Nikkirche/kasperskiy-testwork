import subprocess
import time
from subprocess import Popen

from pydantic.main import BaseModel

class DetailsStat(BaseModel):
    time:str
class Stat(BaseModel):
    isRunning:bool
    details:DetailsStat| None = None
class Cmd_process:

    def __init__(self):
            self.command = None
            self.start_time = None
            self.isRunning = False
            
    def start(self,job:str):
        self.isRunning = True
        self.command = subprocess.Popen(job.split(" "))
        self.start_time = time.time()
    def stop(self):
        self.command.kill()
        self.isRunning = False
    def stat(self):
        if self.isRunning:
            return Stat(self.isRunning)
        else:
            return Stat(self.isRunning)