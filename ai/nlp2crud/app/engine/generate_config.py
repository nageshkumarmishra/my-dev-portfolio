import os
import json
from app.core.llm_client import parse_prompt_to_config_llm

def generate_config(prompt: str, path: str = "examples/config.json"):
    if os.path.exists(path):
        print(f"🗑️ Deleting old config file at {path}")
        os.remove(path)

    print("🔁 Calling LLM to generate new config...")
    config = parse_prompt_to_config_llm(prompt)

    print("📥 LLM returned config:")
    print(json.dumps(config, indent=2))  # Pretty print for debugging

    print("💾 Writing new config to disk...")
    with open(path, "w") as f:
        json.dump(config, f, indent=2)

    return config
