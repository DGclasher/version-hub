import secrets
from typing import Annotated
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials

from app.config import API_USERNAME, API_PASSWORD

security = HTTPBasic()

def authenticate(credentials: Annotated[HTTPBasicCredentials, Depends(security)]) -> str:
    username_correct = secrets.compare_digest(credentials.username, API_USERNAME)
    password_correct = secrets.compare_digest(credentials.password, API_PASSWORD)
    if not (username_correct and password_correct):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username