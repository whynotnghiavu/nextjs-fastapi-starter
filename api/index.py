from fastapi import FastAPI

app = FastAPI(
    docs_url="/docs",
    openapi_url="/openapi.json"
)


@app.get("/api/py/helloFastApi")
def hello_fast_api():
    return {"message": "Hello from FastAPI"}


@app.get("/api/py/xxxxxxxxxx")
def hello_fast_api():
    return {"message": "Hello from xxxxxxxxxx"}
