from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# URL do banco de dados (SQLite para desenvolvimento)
SQLALCHEMY_DATABASE_URL = "sqlite:///./tasks.db"

# Configuração do Engine
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Sessão de banco de dados
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para os modelos declarativos
Base = declarative_base()

# Dependência para obter a sessão do banco nas rotas
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()