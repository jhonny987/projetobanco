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

# Rota para criar um cliente
@router.post("/clientes/", response_model=schemas.ClienteOut)
def create_cliente(cliente: schemas.ClienteCreate, db: Session = Depends(get_db)):
    return crud.create_cliente(db=db, cliente=cliente)

# Rota para listar todos os itens
@router.get("/clientes/", response_model=list[schemas.ClienteOut])
def list_clientes(db: Session = Depends(get_db)):
    return crud.get_clientes(db)

# Rota para pegar um cliente pelo ID
@router.get("/clientes/{cliente_id}", response_model=schemas.ClienteOut)
def get_cliente(cliente_id: int, db: Session = Depends(get_db)):
    cliente = crud.get_cliente(db, cliente_id)
    if not cliente:
        raise HTTPException(status_code=404, detail="cliente não encontrado")
    return cliente

# Rota para deletar um cliente
@router.delete("/clientes/{cliente_id}")
def delete_cliente(cliente_id: int, db: Session = Depends(get_db)):
    cliente = crud.delete_cliente(db, cliente_id)
    if not cliente:
        raise HTTPException(status_code=404, detail="cliente não encontrado")
    return {"message": "cliente deletado com sucesso"}