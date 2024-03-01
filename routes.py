from fastapi import APIRouter, Depends
from typing import Annotated
from schemas import STaskAdd
from repositories import TaskRepository

router = APIRouter(
    prefix="/tasks",
    tags=["tasks"]  # добавляем тег для отображения в Swagger UI
)

@router.post("")
async def create_task(task: Annotated[STaskAdd, Depends()]):
    task_id = await TaskRepository.add_task(task)
    return {"task_id": task_id}

@router.get("")
async def get_tasks():
    tasks = await TaskRepository.get_tasks()
    return {"data": tasks}