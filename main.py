import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from context_module.mcp_context import load_context, save_context
from agents.planner_agent import planner_agent
from agents.researcher_agent import researcher_agent


def main():
    context = load_context()

    if not context.get("user_task"):
        context["user_task"] = input("Enter the task you want help with: ")

    print("\nRunning Planner Agent...")
    context = planner_agent(context)

    print("\nRunning Researcher Agent (Claude)...")
    context = researcher_agent(context)


    save_context(context)

    print("\n Updated Shared Context:")
    for key, value in context.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    main()