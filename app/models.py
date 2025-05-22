from sqlalchemy import Column, Integer, String
from .database import Base

# Define a tabela Item no banco, com o id e descricao
class Item(Base):
    __tablename__ = "itens" # Nome da tabela

    id = Column(Integer, primary_key=True, index=True)
    descricao = Column(String, index=True)