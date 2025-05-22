from sqlalchemy import Column, Integer, String, Date
from .database import Base

# Define a tabela Clientes no banco, com todos seus atributos
class Cliente(Base):
    __tablename__ = "clientes" # Nome da tabela

    id = Column(Integer, primary_key=True, index=True)
    primeiroNome = Column(String, index=False)
    ultimoNome = Column(String, index=False)
    dataNascimento = Column(Date, index=False)
    cpf = Column(String, index=False)