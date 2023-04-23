import os
import resource
import signal
import subprocess
import time
from pathlib import Path

import psutil as psutil

from .models import DetailsStat, Stat
from .utils import file_name


class CmdProcess:

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
                        details=DetailsStat(time=time.time() - self.start_time,
                                            memory=
                                            resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024),
                        system_time=psutil.Process(self.command.pid).cpu_times().system.is_integer())
        else:
            return Stat(isRunning=self.isRunning)
