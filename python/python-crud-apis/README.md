
# 🧰 Python CRUD APIs: Flask vs FastAPI

This repository provides two fully functional Employee CRUD APIs using:

- ✅ Flask (synchronous, traditional web framework)
- ⚡ FastAPI (modern, async-ready framework)

Both APIs demonstrate clean architecture, SQLAlchemy ORM, modular structure, Swagger UI, and unit tests.


# 🗂️ Project Folder Structure

```
python-crud-apis/
├── flask_crud_app/
│   ├── requirements.text
│   ├── app/
│   │   ├── db.py
│   │   ├── run.py
│   │   ├── __init__.py
│   │   ├── models/
│   │   │   └── employee.py
│   │   ├── routes/
│   │   │   └── employee_routes.py
│   │   ├── services/
│   │   │   └── employee_service.py
│   ├── test/
│   │   └── test_employee.py
│   ├── ven_flask/
│       └── (virtual environment files)
├── fastapi_crud_app/
│   ├── requirements.txt
│   ├── app/
│   │   ├── db.py
│   │   ├── main.py
│   │   ├── models/
│   │   │   └── employee.py
│   │   ├── routes/
│   │   │   └── employee_routes.py
│   │   ├── schemas/
│   │   │   └── employee_schema.py
│   │   ├── services/
│   │   │   └── employee_service.py
│   ├── test/
│   │   └── test_employee.py
```


---

## ▶️ Getting Started

### 🐍 Create separate virtual environments for each app

```bash
# Flask env
cd flask_crud_app
python -m venv venv_flask
source venv_flask/bin/activate
pip install -r requirements.text
python run.py
```

Visit: http://127.0.0.1:5000/apidocs

```bash
# FastAPI env
cd fastapi_crud_app
python -m venv venv_fastapi
source venv_fastapi/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Visit: http://127.0.0.1:8000/docs

---

## 🧠 Key Features (in both apps)

- ✅ CRUD operations for Employee entity
- ✅ SQLite + SQLAlchemy
- ✅ Modular architecture (routes, services, models)
- ✅ API documentation (Swagger)
- ✅ Unit tests with Pytest

---

## ⚠️ Error Handling

### Flask
- Uses get_or_404() for missing resources
- Custom handlers can be added via @app.errorhandler

### FastAPI
- Uses HTTPException for all controlled errors
- Automatic 422 validation via Pydantic schemas

---

## 📦 Tech Stack Comparison

| Feature             | Flask                           | FastAPI                       |
|---------------------|----------------------------------|-------------------------------|
| Language Style      | Classic sync                    | Async-first                   |
| ORM                 | SQLAlchemy                      | SQLAlchemy                    |
| Validation          | Manual or WTForms               | Automatic via Pydantic        |
| Swagger             | Flasgger                        | Built-in                      |
| Modularity          | Blueprints + services           | Routers + dependencies        |
| Testing             | flask.test_client()             | TestClient()                  |
| Async Support       | ❌ (Flask 2.x partial)          | ✅ Fully supported             |

---

## 🧪 Run Tests

```bash
# From root folder or respective subfolders
pytest
```

---

## 📬 Author

**Nagesh Kumar Mishra**  

---

## ⚙️ Pydantic v2 Note (FastAPI)

If you're using **Pydantic v2**, update your schema config like this:

```python
from pydantic import ConfigDict

class EmployeeResponse(EmployeeBase):
    id: int
    model_config = ConfigDict(from_attributes=True)
```

This replaces the old Pydantic v1 style:

```python
class Config:
    orm_mode = True
```

---

## ✅ Status

- [x] Flask CRUD app working
- [x] FastAPI CRUD app working
- [x] Modular architecture
- [x] Swagger + auto-docs
- [x] Unit tests
- [x] Clean README for GitHub

