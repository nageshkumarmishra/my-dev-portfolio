from urllib.response import addbase
from app.models.employee import Employee
from  app.db import db

# Business logic for employee CRUD operations

def create_employee(data):
    """Create and persist a new employee."""
    emp=Employee(**data)
    db.session.add(emp)
    db.session.commit()
    return emp

def get_all_employees():
    """Retrieve all employee records."""
    return Employee.query.all()

def get_employee(byemp_id):
    """Retrieve  employee by emp_id record."""
    emp = Employee.query.get_or_404(byemp_id)
    return emp

def update_employee(emp_id, data):
    """Update employee record with new data."""
    emp = Employee.query.get_or_404(emp_id)
    emp.name = data.get('name',emp.name)
    emp.department = data.get('department', emp.department)
    db.session.commit()
    return emp

def delete_employee(emp_id):
    """Delete employee by ID."""
    emp = Employee.query.get_or_404(emp_id)
    db.session.delete(emp)
    db.session.commit()
    return emp


