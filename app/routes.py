from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from . import crud, schemas, database

# Cria o roteador para as rotas
router = APIRouter()

# Dependênciaque cria uma sessão do banco e fecha depois
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Rota para criar um item
@router.post("/items/", response_model=schemas.ItemOut)
def create_item(item: schemas.ItemCreate, db: Session = Depends(get_db)):
    return crud.create_item(db=db, item=item)

# Rota para listar todos os itens
@router.get("/items/", response_model=list[schemas.ItemOut])
def list_items(db: Session = Depends(get_db)):
    return crud.get_items(db)

# Rota para pegar um item pelo ID
@router.get("/items/{item_id}", response_model=schemas.ItemOut)
def get_item(item_id: int, db: Session = Depends(get_db)):
    item = crud.get_item(db, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item não encontrado")
    return item

# Rota para deletar um item
@router.delete("/items/{item_id}")
def delete_item(item_id: int, db: Session = Depends(get_db)):
    item = crud.delete_item(db, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item não encontrado")
    return {"message": "item deletado com sucesso"}