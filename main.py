from fastapi import FastAPI
from pydantic import BaseModel
import models
from db import engine, Base
from routes.user_routes import router as user_router

app = FastAPI()

app.include_router(user_router)

Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"Hello": "World"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
