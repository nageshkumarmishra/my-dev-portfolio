from fastapi import FastAPI
from app.routes.employee_routes import router as employee_router
from app.db import engine, Base

# Create all tables
Base.metadata.create_all(bind=engine)

# Initialize app
app = FastAPI(title="Employee API", version="1.0")

# Register routes
app.include_router(employee_router, prefix="/employees", tags=["Employees"])