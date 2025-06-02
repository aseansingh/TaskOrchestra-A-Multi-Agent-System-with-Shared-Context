import json
import os

def history_viewer_agent(context):
    history_path = "history.json"

    if not os.path.exists(history_path):
        print("\n No history found.")
        context["history"] = []
        return context

    with open(history_path, "r", encoding="utf-8") as f:
        try:
            history = json.load(f)
        except json.JSONDecodeError:
            print("\n Error reading history.json. Please check the file format.")
            context["history"] = []
            return context

    if not history:
        print("\n History is empty.")
    else:
        print("\n Task History (latest first):")
        for i, entry in enumerate(reversed(history), 1):
            print(f"\n--- Entry {i} ---")
            print(f"Task: {entry.get('user_task')}")
            print(f"Plan: {entry.get('plan')}")
            print(f"Summary: {entry.get('summary')}")
            print(f"Result: {entry.get('execution_result')}")

    context["history"] = history
    return context