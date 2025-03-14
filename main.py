import json
import os
from fastapi import FastAPI
import uvicorn

from llm_functions.memory import memory_assessment

app = FastAPI()

@app.get("/hello")
def hello_world():
    return {'message':'hello'}

@app.get("/memory")
async def memory_assessment_endpoint():
    response = await memory_assessment()
    data_dict = json.loads(response)
    return data_dict

@app.get("/logical")
async def logical_assessment_endpoint():
    response = await memory_assessment()
    data_dict = json.loads(response)
    return data_dict

if __name__ == "__main__":
    port = int(os.getenv("PORT"))
    uvicorn.run(app, host="0.0.0.0", port=port)