from pydantic import BaseModel

# Define como os dados chegam na API (entrada)
class ItemCreate(BaseModel):
    descricao: str

# Define como os dados são devolvidos pela API (saída)
class ItemOut(BaseModel):
    id: int
    descricao: str
    
    class Config:
        orm_mode = True # Importante para ler modelos IRM como dicionários