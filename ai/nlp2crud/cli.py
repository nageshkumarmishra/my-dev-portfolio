import os
import sys
import json
import argparse
import uvicorn

from app.engine.generate_config import generate_config
from app.adapters.database import init_engine, sessionmaker
from app.core.config_loader import ConfigLoader
from app.engine.model_generator import generate_model, Base
from app.engine.schema_generator import generate_schemas
from app.engine.router_generator import generate_crud_router
from app.adapters.database import engine

CONFIG_PATH = "./examples/config.json"

def cli_generate(prompt: str):
    """Generate config from prompt using LLM."""
    if os.path.exists(CONFIG_PATH):
        print(f"🗑️ Deleting old config file at {CONFIG_PATH}")
        os.remove(CONFIG_PATH)

    print(f"🔁 Generating config from prompt: '{prompt}'")
    config = generate_config(prompt, path=CONFIG_PATH)

    with open(CONFIG_PATH, "w") as f:
        json.dump(config, f, indent=2)

    print("✅ Config written to", CONFIG_PATH)
    return config

def cli_run_server():
    """Load config, generate code, initialize DB, and launch FastAPI server."""
    if not os.path.exists(CONFIG_PATH):
        print(f"❌ Config file not found at {CONFIG_PATH}. Run the CLI with a prompt first.")
        sys.exit(1)

    print("📄 Loading config...")
    config = ConfigLoader(CONFIG_PATH).load()

    print("🔌 Initializing DB engine...")
    init_engine(config["database"]["url"])

    print("🧱 Generating models...")
    models = []
    for idx, model_config in enumerate(config["models"]):
        try:
            model = generate_model(model_config)
            models.append((model_config, model))
            print(f"✅ Generated model: {model_config['name']}")
        except Exception as e:
            print(f"❌ Failed to generate model at index {idx}: {e}")

    print("📚 Syncing DB tables...")
    Base.metadata.create_all(bind=engine)

    print("🧾 Generating schemas and CRUD routers...")
    from main import app  # Ensure FastAPI app is imported only after model generation

    for model_config, model in models:
        create_schema, update_schema, response_schema = generate_schemas(model_config)
        generate_crud_router(app, model_config, model, create_schema, update_schema, response_schema)

    print("🚀 Launching FastAPI server...")
    os.environ["NLP2CRUD_CONFIG"] = CONFIG_PATH
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="🧠 NLP-to-CRUD CLI")
    parser.add_argument("prompt", type=str, help="Natural language description of API")
    parser.add_argument("--run", action="store_true", help="Run the FastAPI server after generation")
    args = parser.parse_args()

    print("🧠 Received Prompt:", args.prompt)
    cli_generate(args.prompt)

    if args.run:
        cli_run_server()