from fastapi import Depends, HTTPException, Header
import os

API_KEY = os.getenv("API_KEY", "super-secret-key")
AUTH_ENABLED = os.getenv("AUTH_ENABLED", "true").lower() == "true"

def verify_api_key(x_api_key: str = Header(default=None)):
    if not AUTH_ENABLED:
        return
    if not x_api_key or x_api_key != API_KEY:
        raise HTTPException(status_code=403, detail="Invalid or missing API key")