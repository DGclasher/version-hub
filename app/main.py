from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import client, projects_collection
from app.routes.projects import router as projects_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await client.admin.command("ping")
    await projects_collection.create_index("project_name", unique=True)
    yield
    await client.close()

app = FastAPI(
    title="Version Hub API",
    description="API for managing project versions",
    version="1.0.0",
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(projects_router)


@app.get("/health")
async def health_check():
    return {"status": "healthy"}
