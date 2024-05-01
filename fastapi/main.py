from fastapi import FastAPI
from routers import examples, heartbeat

app = FastAPI() 

app.include_router(examples.examples_api)
app.include_router(heartbeat.heartbeat_api)