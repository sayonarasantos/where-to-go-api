from fastapi import FastAPI

# from . import database

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello World!"}


# database.TestConnection()