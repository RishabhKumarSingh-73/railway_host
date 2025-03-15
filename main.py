import json
import os
import re
from fastapi import FastAPI
from openai import OpenAI
import uvicorn

from llm_functions.memory import memory_assessment,logical_assessment,comprehension_assessment,topic_assessment

app = FastAPI()

api_key = os.getenv("API_KEY")

print(api_key)

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key = api_key,
    )

@app.get("/hello")
def hello_world():
    return {'message':'hello'}

@app.get("/memory")
async def memory_assessment_endpoint():
    response = await memory_assessment(client)
    data_dict = json.loads(extract_json(response))
    return data_dict

@app.get("/logical")
async def logical_assessment_endpoint():
    response = await logical_assessment(client)
    data_dict = json.loads(extract_json(response))
    return data_dict

@app.get("/comprehension")
async def comprehension_assessment_endpoint():
    response = await comprehension_assessment(client)
    data_dict = json.loads(extract_json(response))
    return data_dict

@app.get("/topic/{topic}")
async def comprehension_assessment_endpoint(topic:str):
    response = await topic_assessment(client,topic)
    data_dict = json.loads(extract_json(response))
    return data_dict




def extract_json(response: str) -> str:
    
    match = re.search(r'\{.*\}', response, re.DOTALL)  # Match anything between the first and last curly braces
    if match:
        json_str = match.group(0)  # Extract the matched JSON string
        return json_str.strip()  # Remove leading/trailing spaces
    else:
        raise ValueError("No valid JSON found in the response.")

if __name__ == "__main__":
    port = int(os.getenv("PORT"))
    uvicorn.run(app, host="0.0.0.0", port=port)