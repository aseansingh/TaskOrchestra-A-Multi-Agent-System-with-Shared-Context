import os
from dotenv import load_dotenv
from anthropic import Anthropic, HUMAN_PROMPT, AI_PROMPT

load_dotenv()
anthropic = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

def researcher_agent(context):
    task = context.get("user_task", "No task provided")

    prompt = (
        f"{HUMAN_PROMPT} Please research the following task and provide a brief overview:\n\n{task}\n\n{AI_PROMPT}"
    )

    try:
        response = anthropic.completions.create(
            model="claude-3-sonnet-20240229", 
            max_tokens_to_sample=500,
            prompt=prompt,
            temperature=0.7,
        )
        research = response.completion.strip()
        context["research"] = research
        return context

    except Exception as e:
        print(f"❌ Error calling Claude API: {e}")
        context["research"] = "Error: Unable to generate research."
        return context