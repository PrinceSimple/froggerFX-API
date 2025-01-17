from fastapi import FastAPI
from api.players import players
from api.db import metadata, database, engine

metadata.create_all(engine)

app = FastAPI()

 
@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


app.include_router(players)