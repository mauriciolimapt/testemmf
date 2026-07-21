from pydantic import BaseModel, Field
from typing import Optional

# Schema base compartilhado
class TaskBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=255, description="Título da tarefa")
    completed: bool = False

# Schema para CRIAÇÃO
class TaskCreate(TaskBase):
    completed: bool = False

# Schema para ATUALIZAÇÃO (campos opcionais)
class TaskUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=1, max_length=255)
    completed: Optional[bool] = None

# Schema de RESPOSTA
class TaskResponse(TaskBase):
    id: int

    class Config:
        from_attributes = True