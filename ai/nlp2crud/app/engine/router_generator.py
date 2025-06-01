from fastapi import APIRouter, Depends, HTTPException, status, FastAPI
from sqlalchemy.orm import Session
from typing import Type, Callable
from app.adapters.database import get_db

def generate_crud_router(
    app: FastAPI,
    model_config: dict,
    model: Type,
    CreateSchema: Type,
    UpdateSchema: Type,
    ResponseSchema: Type,
    get_session_local: Callable = get_db
) -> APIRouter:
    router = APIRouter()
    model_name = model_config["name"]
    endpoint = f"/{model_name.lower()}s"

    @router.post("/", response_model=ResponseSchema)
    def create_item(payload: CreateSchema, db: Session = Depends(get_session_local)):
        db_item = model(**payload.dict())
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
        return db_item

    @router.get("/", response_model=list[ResponseSchema])
    def read_all_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_session_local)):
        return db.query(model).offset(skip).limit(limit).all()

    @router.get("/{item_id}", response_model=ResponseSchema)
    def read_item(item_id: int, db: Session = Depends(get_session_local)):
        item = db.query(model).get(item_id)
        if item is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return item

    @router.put("/{item_id}", response_model=ResponseSchema)
    def update_item(item_id: int, payload: UpdateSchema, db: Session = Depends(get_session_local)):
        item = db.query(model).get(item_id)
        if item is None:
            raise HTTPException(status_code=404, detail="Item not found")
        for key, value in payload.dict(exclude_unset=True).items():
            setattr(item, key, value)
        db.commit()
        db.refresh(item)
        return item

    @router.delete("/{item_id}")
    def delete_item(item_id: int, db: Session = Depends(get_session_local)):
        item = db.query(model).get(item_id)
        if item is None:
            raise HTTPException(status_code=404, detail="Item not found")
        db.delete(item)
        db.commit()
        return {"message": f"{model_name} deleted successfully"}

    app.include_router(router, prefix=endpoint, tags=[model_name])
    return router  # ✅ Important: return the APIRouter