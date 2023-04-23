from pydantic import BaseModel


class Result(BaseModel):
    output: str | None = None
    err: str | None = None


class DetailsStat(BaseModel):
    time: str


class Stat(BaseModel):
    isRunning: bool
    details: DetailsStat | None = None
