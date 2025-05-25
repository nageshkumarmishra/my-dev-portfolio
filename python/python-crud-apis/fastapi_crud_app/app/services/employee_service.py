from sqlalchemy.orm import Session
from app.models.employee import Employee
from app.schemas.employee_schema import EmployeeCreate, EmployeeUpdate


def get_employees(db: Session):
    return db.query(Employee).all()

def create_employee(db: Session, emp: EmployeeCreate):
    db_emp = Employee(**emp.dict())
    db.add(db_emp)
    db.commit()
    db.refresh(db_emp)
    return db_emp

def update_employee(db: Session, emp_id: int, emp_data: EmployeeUpdate):
    emp = db.query(Employee).filter(Employee.id == emp_id).first()
    if emp:
        for key, value in emp_data.dict().items():
            setattr(emp, key, value)
        db.commit()
        db.refresh(emp)
    return emp


def delete_employee(db: Session, emp_id: int):
    emp = db.query(Employee).filter(Employee.id == emp_id).first()
    if emp:
        db.delete(emp)
        db.commit()
    return emp
