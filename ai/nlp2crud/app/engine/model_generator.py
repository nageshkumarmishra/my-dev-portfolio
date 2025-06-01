import re
import inflect
from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
TYPE_MAP = {
    "int": Integer,
    "str": String,
    "float": Float,
    "bool": Boolean,
    "datetime": DateTime,
}

inflector = inflect.engine()

def generate_model(model_config):
    name_camel = model_config["name"]
    fields = model_config["fields"]

    # Convert CamelCase to snake_case
    name_snake = re.sub(r"(?<!^)(?=[A-Z])", "_", name_camel).lower()
    table_name = inflector.plural(name_snake)

    attrs = {
        "__tablename__": table_name,
        "__table_args__": {"extend_existing": True},
    }

    for field_name, field_def in fields.items():
        column_type = TYPE_MAP.get(field_def["type"])
        kwargs = {}
        if field_def.get("primary_key"):
            kwargs["primary_key"] = True
        if "default" in field_def:
            kwargs["default"] = field_def["default"]
        if "unique" in field_def:
            kwargs["unique"] = field_def["unique"]
        if "nullable" in field_def:
            kwargs["nullable"] = field_def["nullable"]

        if "foreign_key" in field_def:
            fk = field_def["foreign_key"]
            if isinstance(fk, dict) and "referring_table" in fk and "field" in fk:
                ref_table = f"{fk['referring_table'].lower()}s.{fk['field']}"
                attrs[field_name] = Column(column_type, ForeignKey(ref_table), **kwargs)
            else:
                raise ValueError(f"Invalid foreign_key format for field '{field_name}': {fk}")
        else:
            attrs[field_name] = Column(column_type, **kwargs)

    print(f"✅ Generating model: {name_camel} -> table: {table_name}")
    return type(name_camel, (Base,), attrs)