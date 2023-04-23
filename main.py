from fastapi import FastAPI
import docker

app = FastAPI()
client = docker.from_env()


@app.get("/api/phoronix-perf")
async def create_phoronix_perf_process():
    client.containers.run("main", "phoronix-test-suite batch-run  perf-bench", detach=True)
