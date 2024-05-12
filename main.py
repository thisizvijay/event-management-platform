import uvicorn
from fastapi import FastAPI

app= FastAPI()

@app.get("/ping")
async def ping():
    return {"message":"pong"}

@app.get("/test")
async def pong():
    return {"message":"hello"}

@app.get("/vijay")
async def pong():
    return {"message":"Vijay"}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)