# TaskOrchestra – A Multi-Agent System with Shared Context

TaskOrchestra is a modular, AI-powered multi-agent system built with FastAPI and React. It coordinates autonomous agents (Planner, Researcher, Summarizer, Executor, History Viewer) to perform tasks using a shared context. The UI allows users to input tasks, trigger agent collaboration, and view detailed execution results and history.

---

## Features

* **Multi-agent orchestration pipeline**
* **Task planning, research, summarization, and execution**
* **Persistent shared context with history tracking**
* **FastAPI backend with REST endpoints**
* **React frontend to interact with the system visually**
* **Supports exporting task results and summaries**

---

## Folder Structure

```
├── main.py                  # FastAPI entry point
├── orchestrator.py          # Core pipeline logic
├── context_module/
│   └── mcp_context.py       # Load/save shared context
├── agents/
│   ├── planner_agent.py
│   ├── researcher_agent.py
│   ├── summarizer_agent.py
│   ├── executor_agent.py
│   └── history_viewer_agent.py
├── history.json             # Stores past task runs
├── taskorchestra-ui/        # React frontend
│   ├── public/
│   ├── src/
│   │   └── App.jsx, etc.
```

---

## Getting Started

### Backend (FastAPI)

```bash
# Inside the backend root folder
pip install -r requirements.txt
uvicorn main:app --reload
```

### Frontend (React)

```bash
# Inside taskorchestra-ui/
npm install
npm start
```

---

##  API Endpoints

* `POST /run`

```json
{
  "user_task": "python orchestrator.py"
}
```

* `GET /history` – Fetch all previously executed tasks

---

## Deployment

* **Backend**: Deploy FastAPI via Render or Railway
* **Frontend**: Deploy React on Vercel or Netlify

---

## Example Use Case

```
User Input: "Build a Python script that fetches weather data"
-> Planner Agent: Plans the steps
-> Researcher Agent: Gathers online info
-> Summarizer Agent: Extracts key findings
-> Executor Agent: Writes/runs file or opens site
-> History Agent: Saves outcome
