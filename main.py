from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Dict, Any
import uvicorn
import json
import os
from pipeline import run_pipeline  # Reuse your orchestrator pipeline logic

app = FastAPI()

# Enable CORS so your React app can communicate
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Ensure history.json exists
HISTORY_FILE = "history.json"
if not os.path.exists(HISTORY_FILE):
    with open(HISTORY_FILE, "w") as f:
        json.dump([], f, indent=2)

class TaskRequest(BaseModel):
    user_task: str

@app.post("/run")
async def run_task(request: TaskRequest):
    context = {"user_task": request.user_task}
    result = run_pipeline(context)

    # Append to history
    with open(HISTORY_FILE, "r") as f:
        history = json.load(f)
    history.insert(0, {
        "user_task": result.get("user_task"),
        "plan": result.get("plan"),
        "summary": result.get("summary"),
        "research": result.get("research"),
        "execution_result": result.get("execution_result")
    })
    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f, indent=2)

    return result

@app.get("/history")
async def get_history():
    with open(HISTORY_FILE, "r") as f:
        return json.load(f)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)