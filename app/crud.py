from sqlalchemy.orm import Session
from . import models, schemas

# Função para criar um novo cliente
def create_cliente(db: Session, cliente: schemas.ClienteCreate):
    db_cliente = models.cliente(descricao=cliente.descricao)
    db.add(db_cliente)
    db.commit()
    db.refresh(db_cliente)
    return db_cliente

# Função para listar todos os clientes
def get_clientes(db: Session):
    return db.query(models.Cliente).all()

# Função para obter um cliente pelo ID
def get_cliente(db: Session, id: int):
    return db.query(models.Cliente).filter(models.Cliente.id == id).first()

# Função para deletar um cliente pelo ID
def delete_cliente(db: Session, cliente_id: int):
    cliente = db.query(models.Cliente).filter(models.Cliente.id == id).first()
    if cliente:
        db.delete(cliente)
        db.commit()
    return cliente