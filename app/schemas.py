from pydantic import BaseModel
from datetime import datetime

# Define como os dados chegam na API (entrada)
class ClienteCreate(BaseModel):
    primeiroNome: str
    ultimoNome: str
    dataNascimento: datetime
    cpf: str

# Define como os dados são devolvidos pela API (saída)
class ClienteOut(BaseModel):
    id: int
    primeiroNome: str
    ultimoNome: str
    dataNascimento: datetime
    cpf: str
    
    class Config:
        orm_mode = True # Importante para ler modelos IRM como dicionários