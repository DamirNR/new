from fastapi import FastAPI
import socket
import time
app = FastAPI(title="Task docker for OTUS")
hostname=socket.gethostname()
time.sleep (0.9)
@app.get("/health/")
def hello(name: str = ""):
   return {"status": "OK"}, hostname