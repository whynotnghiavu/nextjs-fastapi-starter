from fastapi import FastAPI

app = FastAPI(
    docs_url="/api/py/docs",
    openapi_url="/api/py/openapi.json"
)


@app.get("/api/py/helloFastApi")
def helloFastApi():
    return {"message": "Hello from FastAPI"}


@app.get("/api/py/xxxxxxxxxx")
def xxxxxxxxxx():
    return {"message": "Hello from xxxxxxxxxx"}


@app.get("/api/py/cccccccccc")
def cccccccccc():
    return {"message": "Hello from cccccccccc"}
