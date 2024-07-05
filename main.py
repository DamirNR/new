from fastapi import FastAPI
app = FastAPI(title="Task docker for OTUS")
@app.get("/health/")
def hello(name: str = ""):
   return {"status": "OK"}