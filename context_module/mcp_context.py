import json
from pathlib import Path

# File to store the shared context
CONTEXT_FILE = Path("context_module/context.json")

def load_context():
    """Load shared agent context from disk."""
    if CONTEXT_FILE.exists():
        with open(CONTEXT_FILE, "r") as f:
            return json.load(f)
    return {}

def save_context(context):
    """Save updated context to disk."""
    with open(CONTEXT_FILE, "w") as f:
        json.dump(context, f, indent=2)