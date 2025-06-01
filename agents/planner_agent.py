def planner_agent(context):
    """
    Reads a user task from the shared context and generates a plan.
    """
    task = context.get("user_task", "No task provided")
    
    plan = [
        f"Step 1: Research about '{task}'",
        "Step 2: Summarize key findings",
        "Step 3: Execute actions based on summary"
    ]
    
    context["plan"] = plan
    return context