import os
import json

class ConfigLoader:
    def __init__(self, path: str):
        self.path = path

    def load(self):
        if not os.path.exists(self.path):
            raise FileNotFoundError(f"Config file not found at path: {self.path}")

        print(f"📄 Loading config from {self.path}")
        with open(self.path) as f:
            config = json.load(f)

        if "models" not in config:
            raise ValueError("Config missing 'models' section")
        if "database" not in config:
            raise ValueError("Database configuration is missing")

        return config