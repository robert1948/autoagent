from fastapi import FastAPI
from agent import run_agent

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Autoagent backend is live"}

@app.get("/run-agent")
def trigger_agent():
    run_agent()
    return {"status": "Agent triggered"}
