from fastapi import FastAPI
from transform import *

app = FastAPI(title="Transform text API")

@app.get("/")
def root():
    return {"Message": "API Started"}


@app.post("/transform")
def transform(input: str):
    result = trans_data(input)
    return result