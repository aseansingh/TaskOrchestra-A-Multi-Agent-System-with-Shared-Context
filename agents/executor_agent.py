import os
import webbrowser
import subprocess
import json
from urllib.parse import quote

HISTORY_FILE = "history.json"


def save_to_history(context):
    history = []
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r", encoding="utf-8") as f:
            history = json.load(f)

    history.append({
        "user_task": context.get("user_task", ""),
        "plan": context.get("plan", []),
        "research": context.get("research", ""),
        "summary": context.get("summary", ""),
        "execution_result": context.get("execution_result", "")
    })

    with open(HISTORY_FILE, "w", encoding="utf-8") as f:
        json.dump(history, f, indent=2)


def executor_agent(context):
    plan = context.get("plan", [])
    summary = context.get("summary", "")
    research = context.get("research", "")
    user_task = context.get("user_task", "")

    print("\n Executing Final Plan:")

    if isinstance(plan, list):
        for step in plan:
            print(f"- {step}")

            step_lower = step.lower()

            # Dynamic Google search if step asks to open a URL
            if "open" in step_lower and "url" in step_lower:
                query = quote(user_task)
                search_url = f"https://www.google.com/search?q={query}"
                print(f"  -> Opening search for task in browser: {search_url}")
                webbrowser.open(search_url)

            # Create a file with summary and research
            elif "create" in step_lower and "file" in step_lower:
                filename = context.get("filename", "generated_summary.txt")
                with open(filename, "w", encoding="utf-8") as f:
                    f.write("Summary:\n")
                    f.write(summary + "\n\n")
                    f.write("Research:\n")
                    f.write(research)
                print(f"  -> Created file: {filename} with research and summary")

            # Run a Python script mentioned in the step
            elif "run" in step_lower and ".py" in step_lower:
                words = step_lower.split()
                script_name = next((w for w in words if w.endswith(".py")), None)
                if script_name and os.path.exists(script_name):
                    print(f"  -> Running script: {script_name}")
                    os.system(f"python {script_name}")
                else:
                    print(f"  -> Script {script_name or '[not found]'} not found, skipping.")

            # Clone a GitHub repo if mentioned
            elif "clone" in step_lower and "github.com" in step_lower:
                url_start = step_lower.find("https://github.com")
                if url_start != -1:
                    repo_url = step[step_lower.find("https://github.com"):].split()[0]
                    folder_name = repo_url.split("/")[-1]
                    if not os.path.exists(folder_name):
                        print(f"  -> Cloning repo: {repo_url}")
                        subprocess.run(["git", "clone", repo_url])
                    else:
                        print(f"  -> Repo {folder_name} already cloned.")

            # Install Python packages if step includes pip install
            elif "install" in step_lower and "pip" in step_lower:
                if "pip install" in step_lower:
                    packages = step_lower.split("pip install")[-1].strip().split()
                    for package in packages:
                        print(f"  -> Installing package: {package}")
                        subprocess.run(["pip", "install", package])

    context["execution_result"] = "Execution complete (with real actions)."
    save_to_history(context)
    return context