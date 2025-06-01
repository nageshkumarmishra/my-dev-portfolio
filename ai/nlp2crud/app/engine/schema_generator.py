from pydantic import BaseModel
from typing import Optional, Dict, Any, Type
from datetime import datetime

# Safe Python type map
TYPE_MAP = {
    "int": int,
    "str": str,
    "float": float,
    "bool": bool,
    "datetime": datetime
}

def build_schema_class(
    class_name: str,
    fields: Dict[str, Any],
    *,
    include_primary_keys: bool = False,
    is_optional: bool = False
) -> Type[BaseModel]:
    annotations = {}
    defaults = {}

    for field_name, field_def in fields.items():
        field_type = TYPE_MAP.get(field_def.get("type"))
        if not field_type:
            raise ValueError(f"Unsupported or missing type for field '{field_name}': {field_def}")

        # Skip primary keys if not requested (typically for CreateSchema)
        if not include_primary_keys and field_def.get("primary_key", False):
            continue

        if is_optional or field_def.get("nullable", False):
            annotations[field_name] = Optional[field_type]
        else:
            annotations[field_name] = field_type

        if "default" in field_def:
            defaults[field_name] = field_def["default"]

    return type(class_name, (BaseModel,), {
        "__annotations__": annotations,
        **defaults
    })

def generate_schemas(model_config: dict):
    name = model_config["name"]
    fields = model_config["fields"]

    CreateSchema = build_schema_class(
        f"{name}Create",
        fields,
        include_primary_keys=False,
        is_optional=False
    )

    UpdateSchema = build_schema_class(
        f"{name}Update",
        fields,
        include_primary_keys=False,
        is_optional=True
    )

    ResponseSchema = build_schema_class(
        f"{name}Response",
        fields,
        include_primary_keys=True,
        is_optional=False
    )

    return CreateSchema, UpdateSchema, ResponseSchema