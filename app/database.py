from pymongo import AsyncMongoClient
from pymongo.server_api import ServerApi
from app.config import MONGO_DB_URI, MONGO_DB_NAME

client = AsyncMongoClient(
    MONGO_DB_URI,
    server_api=ServerApi(
        version="1",
        strict=True,
        deprecation_errors=True
    )
)

database = client[MONGO_DB_NAME]

projects_collection = database["projects"]