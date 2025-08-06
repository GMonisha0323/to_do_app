from fastapi import FastAPI
from controller import router  # assuming you have controller.py

app = FastAPI()

app.include_router(router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the To-Do API"}
