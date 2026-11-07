from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/users")
def read_users():
    return {"users": [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]}

@app.get("/users/{user_id}")
def read_user(user_id: int):
    return {"user_id": user_id, "name": f"User {user_id}"}

@app.post("/users")
def create_user(user: dict):
    return {"message": "User created", "user": user}