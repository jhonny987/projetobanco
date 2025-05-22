# Importa SQLAlchemy para gerenciar a conexão e o modelo do banco
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Cria um banco SQLite local chamado 'ProjetoBanco.db'
SQLALCHEMY_DATABASE_URL = "sqlite:///./projetobanco.db"

# Cria o mecanismo de conexão com o banco
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Cria uma sessão para interagir com o banco
SessionLocal = sessionmaker(autocommit=False, autoflush=False,bind=engine)

# Base para criarmos os modelos
Base = declarative_base()