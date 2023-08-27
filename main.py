from fastapi import FastAPI
from dotenv import dotenv_values
from pymongo import MongoClient
from routes import router as book_router

app = FastAPI()
config = dotenv_values(".env")

# @app.get('/')
# async def root():
#     return {'message': 'Welcome to the Pymongo fastapi.'}


@app.on_event('startup')
def startup_db_client():
    app.mongo_client = MongoClient(config["ATLAS_URI"])
    app.database = app.mongo_client[config["DB_NAME"]]
    print("Connected to the MongoDB database!")


@app.on_event('shutdown')
def shutdown_db_client():
    app.mongo_client.close()

app.include_router(book_router, tags=["books"], prefix="/book")


