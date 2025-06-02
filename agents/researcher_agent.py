import os
from dotenv import load_dotenv
from anthropic import Client

load_dotenv()
client = Client(api_key=os.getenv("ANTHROPIC_API_KEY"))

def researcher_agent(context):
    task = context.get("user_task", "No task provided")

    prompt = f"Please research the following task and provide a brief overview:\n\n{task}"

    try:
        response = client.messages.create(
            model="claude-3-haiku-20240307",
            max_tokens=500,
            temperature=0.7,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        research = response.content[0].text.strip()
        context["research"] = research
        return context

    except Exception as e:
        print(f" Error calling Claude API: {e}")
        context["research"] = "Error: Unable to generate research."
        return context