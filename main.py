from fastapi import FastAPI, HTTPException
import docker
from pathlib import Path

app = FastAPI(docs_url="/api/docs", redoc_url=None)
client = docker.from_env()


def get_output_name(prog: str):
    return "".join(prog.split())


@app.post("/api/phoronix-perf")
async def actions_with_phoronix_perf_process(option: str):
    job = "phoronix-test-suite batch-run  perf-bench"
    job_in_containers = client.containers.list(filters={'name': job})
    if option == "start":
        if len(job_in_containers) != 0:
            raise HTTPException(status_code=400, detail="Job is already running!")
        client.containers.run("testbench", command=job + " > " + get_output_name(job), name=job, detach=True)
    elif option == "stop":
        if len(job_in_containers) < 1:
            raise HTTPException(status_code=400, detail="Job is no running!")
        job_in_containers[0].stop()
    else:
        raise HTTPException(status_code=400, detail="Invalid option is given")


@app.get("api/phoronix-perf")
async def status_phoronix_perf_process():
    job = "phoronix-test-suite batch-run  perf-bench"
    job_in_containers = client.containers.list(filters={'name': job})
    if len(job_in_containers) != 0:
        return {1:1}
    else:
        return {0:0}


@app.get("/api/phoronix-perf/result")
async def result_phoronix_perf_process():
    job = "phoronix-test-suite batch-run  perf-bench"
    return  Path(get_output_name(job)).read_text()

