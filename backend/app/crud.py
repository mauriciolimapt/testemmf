from sqlalchemy.orm import Session
from app import models, schemas

def get_all_tasks(db: Session):
    return db.query(models.Task).all()

def get_task_by_id(db: Session, task_id: int):
    return db.query(models.Task).filter(models.Task.id == task_id).first()

def create_task(db: Session, task: schemas.TaskCreate):
    db_task = models.Task(title=task.title, completed=task.completed)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def update_task(db: Session, task_id: int, task_update: schemas.TaskUpdate):
    db_task = get_task_by_id(db, task_id)
    if db_task:
        if task_update.title is not None:
            db_task.title = task_update.title
        if task_update.completed is not None:
            db_task.completed = task_update.completed
        db.commit()
        db.refresh(db_task)
    return db_task

def delete_task(db: Session, task_id: int):
    db_task = get_task_by_id(db, task_id)
    if db_task:
        db.delete(db_task)
        db.commit()
        return True
    return False