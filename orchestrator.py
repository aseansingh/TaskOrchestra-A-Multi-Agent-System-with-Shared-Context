from agents.planner_agent import planner_agent
from agents.researcher_agent import researcher_agent
from context_module.mcp_context import load_context, save_context
from agents.summarizer_agent import summarizer_agent
from agents.executor_agent import executor_agent
from agents.history_viewer_agent import history_viewer_agent
import json

AGENT_PIPELINE = [
    ("Planner Agent", planner_agent),
    ("Researcher Agent", researcher_agent),
    ("Summarizer Agent", summarizer_agent),
    ("Executor Agent", executor_agent),
    ("History Viewer Agent", history_viewer_agent)
]

def run_pipeline(context=None):
    if context is None:
        context = load_context()

    if not context.get("user_task"):
        context["user_task"] = input("Enter the task you want help with: ")

    for name, agent in AGENT_PIPELINE:
        print(f"\n Running {name}...")
        context = agent(context)

    save_context(context)

    print("\n Final Shared Context:")
    for key, value in context.items():
        if isinstance(value, str):
            print(f"{key}: {value}")
        elif isinstance(value, list):
            print(f"{key}:")
            for item in value:
                print(f"  - {item}" if isinstance(item, str) else f"  - {json.dumps(item, indent=2)}")
        else:
            print(f"{key}: {value}")

    return context  # Add return so FastAPI can respond with this data

if __name__ == "__main__":
    run_pipeline()
