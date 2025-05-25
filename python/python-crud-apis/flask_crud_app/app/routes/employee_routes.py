from flask import Blueprint, request, jsonify
from flasgger.utils import swag_from
from app.services.employee_service import (
    create_employee, get_all_employees,
    update_employee, delete_employee,
    get_employee
)

employee_bp = Blueprint('employee_bp', __name__)

# POST /employees - Create a new employee
@employee_bp.route('/', methods=['POST'])
@swag_from({
    'parameters': [{
        'in': 'body',
        'name': 'body',
        'required': True,
        'schema': {
            'type': 'object',
            'properties': {
                'name': {'type': 'string'},
                'department': {'type': 'string'}
            }
        }
    }],
    'responses': {
        201: {'description': 'Employee created'}
    }
})
def add_employee():
    emp = create_employee(request.get_json())
    return jsonify(emp.to_dict()), 201

# GET /employees - Retrieve list of all employees
@employee_bp.route('/', methods=['GET'])
def list_employees():
    emps = get_all_employees()
    return jsonify([e.to_dict() for e in emps])

# GET /employees/<id>  - Retrieve employee from all employees
@employee_bp.route('/<int:emp_id>', methods=['GET'])
def employees_byemp(emp_id):
    emp = get_employee(emp_id)
    return jsonify(emp.to_dict())

# PUT /employees/<id> - Update an existing employee's data
@employee_bp.route('/<int:emp_id>', methods=['PUT'])
def modify_employee(emp_id):
    emp = update_employee(emp_id, request.get_json())
    return jsonify(emp.to_dict())

# DELETE /employees/<id> - Delete employee by ID
@employee_bp.route('/<int:emp_id>', methods=['DELETE'])
def remove_employee(emp_id):
    delete_employee(emp_id)
    return jsonify({"message": "Deleted"}), 200