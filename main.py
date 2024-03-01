from fastapi import FastAPI
from database import create_tables, drop_tables
from contextlib import asynccontextmanager

from routes import router as task_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await drop_tables()
    print("tables dropped")
    await create_tables()
    print("tables created")
    yield
    print("off")

app = FastAPI(lifespan=lifespan)
app.include_router(task_router)
