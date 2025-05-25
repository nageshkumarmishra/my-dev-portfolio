from pydantic import BaseModel, ConfigDict

class EmployeeBase(BaseModel):
    name: str
    department: str

class EmployeeCreate(EmployeeBase):
    pass

class EmployeeUpdate(EmployeeBase):
    pass

class EmployeeResponse(EmployeeBase):
    id: int

    model_config = ConfigDict(from_attributes=True)