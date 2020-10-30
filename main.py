from fastapi import FastAPI
app = FastAPI()
message = {
  "message": "Yo Franky"
}

@app.get("/")
def hello():
  return message