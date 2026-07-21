from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from app.database import engine, Base
from app.routers import tasks

# Cria as tabelas no banco de dados ao iniciar
Base.metadata.create_all(bind=engine)

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Código de inicialização (se necessário)
    yield
    # Código de finalização (se necessário)

app = FastAPI(
    title="ATLIN Task Backend API",
    description="API para gerenciamento de tarefas, compatível com frontend React/Vite",
    version="1.0.0",
    lifespan=lifespan
)

# Configuração de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Porta do Vite
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Inclusão das rotas
app.include_router(tasks.router)

@app.get("/")
def root():
    return {"message": "ATLIN Task Backend API is running"}