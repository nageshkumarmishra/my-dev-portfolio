from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db import SessionLocal
from app.schemas.employee_schema import *
from app.services.employee_service import *

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/", response_model= list[EmployeeResponse])
def list_employees(db: Session = Depends(get_db)):
    return get_employees(db)

@router.post("/", response_model=EmployeeResponse, status_code=201)
def create(emp: EmployeeCreate, db: Session = Depends(get_db)):
    return create_employee(db, emp)

@router.put("/{emp_id}", response_model=EmployeeResponse)
def update(emp_id: int, emp: EmployeeUpdate, db: Session = Depends(get_db)):
    updated = update_employee(db, emp_id, emp)
    if not updated:
        raise HTTPException(status_code=404, detail="Employee not found")
    return updated

@router.delete("/{emp_id}", status_code=204)
def delete(emp_id: int, db: Session = Depends(get_db)):
    deleted = delete_employee(db, emp_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Employee not found")