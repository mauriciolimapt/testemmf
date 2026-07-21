from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app import crud, schemas
from app.database import get_db

router = APIRouter(prefix="/tasks", tags=["Tasks"])

@router.get("/", response_model=list[schemas.TaskResponse], status_code=status.HTTP_200_OK)
def read_tasks(db: Session = Depends(get_db)):
    """Retorna todas as tarefas."""
    return crud.get_all_tasks(db)

@router.post("/", response_model=schemas.TaskResponse, status_code=status.HTTP_201_CREATED)
def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    """Cria uma nova tarefa."""
    return crud.create_task(db=db, task=task)

@router.put("/{task_id}", response_model=schemas.TaskResponse, status_code=status.HTTP_200_OK)
def update_task(task_id: int, task_update: schemas.TaskUpdate, db: Session = Depends(get_db)):
    """Atualiza uma tarefa existente."""
    db_task = crud.update_task(db=db, task_id=task_id, task_update=task_update)
    if db_task is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    return db_task

@router.delete("/{task_id}", status_code=status.HTTP_200_OK)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    """Remove uma tarefa."""
    success = crud.delete_task(db=db, task_id=task_id)
    if not success:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    return {"message": "Task deleted."}