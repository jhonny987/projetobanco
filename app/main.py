from fastapi import FastAPI
from . import models, database, routes

# Cria a estrutura das tabelas no banco de dados
models.Base.metadata.create_all(bind=database.engine)

# Cria a aplicação FastAPI
app = FastAPI()

# Inclui as rotas definidas
app.include_router(routes.router)