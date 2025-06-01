import os
from fastapi import FastAPI
from app.core.config_loader import ConfigLoader
from app.adapters.database import init_engine
from app.engine.model_generator import generate_model
from app.engine.schema_generator import generate_schemas
from app.engine.router_generator import generate_crud_router

config_path = os.getenv("NLP2CRUD_CONFIG", "./examples/config.json")
config = ConfigLoader(config_path).load()

init_engine(config["database"]["url"])
app = FastAPI()

@app.get("/")
def root():
    return {"message": "🚀 NLP2CRUD API is running"}

for model_cfg in config["models"]:
    model = generate_model(model_cfg)
    create_schema, update_schema, response_schema = generate_schemas(model_cfg)
    router = generate_crud_router(app, model_cfg, model, create_schema, update_schema, response_schema)
    app.include_router(router, prefix=f"/{model_cfg['name'].lower()}s")