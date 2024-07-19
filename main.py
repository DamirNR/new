from fastapi import FastAPI
import socket
app = FastAPI(title="Task docker for OTUS")
@app.get("/health/")
def hello(name: str = ""):
   return {"status": "OK"}