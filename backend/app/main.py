from fastapi import FastAPI
from app.api.health import router as health

app = FastAPI()


app.include_router(health)


@app.get("/")
def read_root():
    return {"Hello": "World"}
