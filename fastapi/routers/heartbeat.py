from fastapi import APIRouter

heartbeat_api = APIRouter()

@heartbeat_api.get("/")
async def test():
    return {"message": "Hello World"}
