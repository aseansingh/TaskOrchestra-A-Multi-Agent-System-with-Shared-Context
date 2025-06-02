import os
import webbrowser
from urllib.parse import quote


def executor_agent(context):
    plan = context.get("plan", [])
    summary = context.get("summary", "")
    research = context.get("research", "")

    print("\n Executing Final Plan:")

    if isinstance(plan, list):
        for step in plan:
            print(f"- {step}")

            step_lower = step.lower()

            # Open a relevant URL if research contains URLs or topics
            if "open" in step_lower and "url" in step_lower:
                query = quote(context.get("user_task", "AI agent"))
                search_url = f"https://www.google.com/search?q={query}"
                print(f"  -> Opening search for task in browser: {search_url}")
                webbrowser.open(search_url)

            # Create a file with summary content
            elif "create" in step_lower and "file" in step_lower:
                filename = context.get("filename", "generated_summary.txt")
                with open(filename, "w", encoding="utf-8") as f:
                    f.write("Summary:\n")
                    f.write(summary + "\n\n")
                    f.write("Research:\n")
                    f.write(research)
                print(f"  -> Created file: {filename} with research and summary")

            # Try to run a referenced script
            elif "run" in step_lower and ".py" in step_lower:
                words = step_lower.split()
                script_name = next((w for w in words if w.endswith(".py")), None)
                if script_name and os.path.exists(script_name):
                    print(f"  -> Running script: {script_name}")
                    os.system(f"python {script_name}")
                else:
                    print(f"  -> Script {script_name or '[not found]'} not found, skipping.")

    context["execution_result"] = "Execution complete (with enhanced logic)."
    return context