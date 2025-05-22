from sqlalchemy.orm import Session
from . import models, schemas

# Função para criar um novo item
def create_item(db: Session, item: schemas.ItemCreate):
    db_item = models.Item(descricao=item.descricao)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

# Função para listar todos os itens
def get_items(db: Session):
    return db.query(models.Item).all()

# Função para obter um item pelo ID
def get_item(db: Session, item_id: int):
    return db.query(models.Item).filter(models.Item.id == item_id).first()

# Função para deletar um item pelo ID
def delete_item(db: Session, item_id: int):
    item = db.query(models.Item).filter(models.Item.id == item_id).first()
    if item:
        db.delete(item)
        db.commit()
    return item