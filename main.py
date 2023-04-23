from fastapi import FastAPI
import docker

app = FastAPI(docs_url="/api/docs", redoc_url=None)
client = docker.from_env()


@app.post("/api/phoronix-perf")
async def create_phoronix_perf_process(option:str):
    job ="phoronix-test-suite batch-run  perf-bench"
    if(option=="start"):
        client.containers.run("main",job , detach=True)
    elif(option=="stop"):
        pass
    else:
        pass
@app.get("api/phoronix-perf")
async def status_phoronix_perf_process():
    pass
@app.get("/api/phoronix-perf/result")
async def result_phoronix_perf_process():
    pass