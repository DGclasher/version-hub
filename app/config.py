import os
from dotenv import load_dotenv

load_dotenv()

MONGO_DB_URI = os.environ["MONGO_DB_URI"]
MONGO_DB_NAME = os.environ["MONGO_DB_NAME"]

API_USERNAME = os.environ["API_USERNAME"]
API_PASSWORD = os.environ["API_PASSWORD"]
