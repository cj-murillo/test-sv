from fastapi import FastAPI
from app import __version__

app = FastAPI(
    title="Mi API Interna",
    version=__version__,  # Esto actualiza la versión visible en Swagger
)


@app.get("/version")
def get_version():
    return {"version": __version__}

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI app"}


@app.get("/add")
def add(a: float, b: float):
    return {"result": a + b}


@app.get("/subtract")
def subtract(a: float, b: float):
    return {"result": a - b}


@app.get("/multiply")
def multiply(a: float, b: float):
    return {"result": a * b}


@app.get("/divide")
def divide(a: float, b: float):
    if b == 0:
        return {"error": "Division by zero is not allowed"}
    return {"result": a / b}
