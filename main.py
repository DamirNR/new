from fastapi import FastAPI
import socket
import time
app = FastAPI(title="Task docker for OTUS")
hostname=socket.gethostname()
time.sleep (30.0)
@app.get("/health/")
def hello(name: str = ""):
   return {"status": "OK"}, hostname