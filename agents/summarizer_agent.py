import os
from dotenv import load_dotenv
from anthropic import Client

load_dotenv()
client = Client(api_key=os.getenv("ANTHROPIC_API_KEY"))

def summarizer_agent(context):
    research = context.get("research", "")

    if not research:
        context["summary"] = "No research available to summarize."
        return context

    prompt = f"Please summarize the following research in a clear, concise way:\n\n{research}"

    try:
        response = client.messages.create(
            model="claude-3-haiku-20240307",
            max_tokens=300,
            temperature=0.5,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        summary = response.content[0].text.strip()
        context["summary"] = summary
        return context

    except Exception as e:
        print(f" Error calling Claude for summary: {e}")
        context["summary"] = "Error: Unable to summarize research."
        return context
