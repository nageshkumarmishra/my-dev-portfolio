import re

# app/core/prompt_parser.py

def parse_prompt_to_config(prompt: str) -> dict:
    """
    Parse user prompt into an intermediate config structure (basic fallback parser).
    """
    # Example: "Create an API for BooksDelivery with book_id, delivery_date, recipient_name"
    import re

    match = re.match(r"create an api for (\w+) with (.+)", prompt.strip().lower())
    if not match:
        raise ValueError("Prompt does not match expected format")

    model_name = match.group(1).title().replace(" ", "")
    fields_str = match.group(2)

    fields = {}
    for field in [f.strip() for f in fields_str.split(",")]:
        field_key = field.lower()
        fields[field_key] = {"type": "str"}  # Default fallback type

    return {
        "model_name": model_name,
        "fields": fields
    }