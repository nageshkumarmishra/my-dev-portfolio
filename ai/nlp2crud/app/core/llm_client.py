import requests
import re
import json
from pydantic import BaseModel, Field, ValidationError
from typing import Dict, List

LLM_SERVER_URL = "http://localhost:1234/v1/chat/completions"
LLM_SYSTEM_PROMPT = """
You are a backend architecture assistant that generates backend config schemas in JSON format based on natural language prompts. Your job is to extract entity names and their fields (with types and constraints) and return a JSON object suitable for dynamic API generation.

Rules:
- Output only a JSON object (do not include explanations or markdown formatting).
- The root object must contain:
  - `database`: with a `url` field (always use \"sqlite:///./app.db\").
  - `models`: a list of model definitions.
- Each model must have:
  - `name`: the model name.
  - `fields`: a dictionary of field names and their metadata.
- Each field definition must include:
  - `type`: one of `str`, `int`, `float`, `bool`, or `datetime`.
  - Optionally: `primary_key`, `unique`, `nullable`, `default`.

Example output for prompt: \"Build an API for user with id, name, and email\":
{
  "database": {
    "url": "sqlite:///./app.db"
  },
  "models": [
    {
      "name": "User",
      "fields": {
        "id": {"type": "int", "primary_key": true},
        "name": {"type": "str"},
        "email": {"type": "str", "unique": true}
      }
    }
  ]
}
"""

class FieldDef(BaseModel):
    type: str = Field(..., description="Data type like str, int, bool, etc.")
    primary_key: bool = False

class ModelDef(BaseModel):
    name: str
    fields: Dict[str, FieldDef]

class ConfigSchema(BaseModel):
    database: Dict[str, str]
    models: List[ModelDef]

def build_user_prompt(prompt: str) -> str:
    return f"Prompt: {prompt}\n\nReturn only the valid config JSON."

def parse_prompt_to_config_llm(prompt: str) -> dict:
    messages = [
        {"role": "system", "content": LLM_SYSTEM_PROMPT},
        {"role": "user", "content": build_user_prompt(prompt)}
    ]

    print("Sending prompt to LLM:", json.dumps(messages, indent=2))

    try:
        response = requests.post(
            LLM_SERVER_URL,
            json={"model": "deepseek-r1-distill-qwen-7b", "messages": messages, "temperature": 0.2},
            timeout=60
        )
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"LLM request failed: {e}")

    result = response.json()
    print("Received LLM response JSON:", json.dumps(result, indent=2))

    if "choices" not in result or not result["choices"]:
        raise ValueError("❌ LLM response does not contain 'choices' or is empty.")

    raw_content = result["choices"][0]["message"]["content"]
    if not raw_content.strip():
        raise ValueError("❌ LLM returned empty content. Please check the prompt or LLM server.")

    print("Raw LLM output content:", raw_content)

    match = re.search(r'{[\s\S]*}', raw_content)
    if not match:
        raise ValueError("❌ Could not extract valid JSON from LLM output.")

    json_str = match.group(0)
    config_dict = extract_json(json_str)

    try:
        validated = ConfigSchema(**config_dict)
    except ValidationError as e:
        raise ValueError(f"❌ Config schema validation failed: {e}")

    model_names = [model.name for model in validated.models]
    print("✅ Extracted model names from config:", model_names)
    return config_dict

def extract_json(text: str) -> dict:
    try:
        match = re.search(r'{.*}', text, re.DOTALL)
        if not match:
            raise ValueError("No JSON object found in LLM output")
        return json.loads(match.group())
    except Exception as e:
        print("❌ JSON extraction failed:", e)
        raise