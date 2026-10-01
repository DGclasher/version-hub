from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from pymongo import ReturnDocument
from app.database import projects_collection
from app.auth import authenticate

router = APIRouter(prefix="/projects", tags=["projects"])

@router.get("/{project_name}/version")
async def get_project_version(project_name: str, _: Annotated[str, Depends(authenticate)]):
    project = await projects_collection.find_one(
            {"project_name": project_name},
            {"_id": 0, "project_name": 1, "current_version": 1}
        )
    if project is None:
        raise HTTPException(status_code=404, detail="Project not found")

    return {
        "project_name": project["project_name"],
        "current_version": project["current_version"]
    }

@router.post("/{project_name}/version")
async def update_project_version(project_name: str, _: Annotated[str, Depends(authenticate)]):
    project = await projects_collection.find_one_and_update(
        {"project_name": project_name},
        {"$inc": {"current_version": 1}},
        projection={"_id": 0, "project_name": 1, "current_version": 1},
        return_document=ReturnDocument.BEFORE
    )
    if project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    return {
        "project_name": project["project_name"],
        "previous_version": project["current_version"],
        "new_version": project["current_version"] + 1
    }
                                 