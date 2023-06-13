from pymongo import MongoClient
from dotenv import dotenv_values

config = dotenv_values(".env")
def get_database():
    CONNECTION_STRING = config['DATABASE_URL']
    client = MongoClient(CONNECTION_STRING)

    return client["salvager"]

if __name__ == "__main__":
    dbname = get_database()