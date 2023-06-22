from pymongo import MongoClient
from dotenv import dotenv_values
import os
config = dotenv_values(".env")
def get_database():
    CONNECTION_STRING =   os.getenv("DATABASE_URL")
    client = MongoClient(CONNECTION_STRING)
    return client["salvager"]

if __name__ == "__main__":
    dbname = get_database()
