from fastapi import FastAPI
from src.chat.routers import router as router_chat
from src.users.routers import router as router_user

app = FastAPI()

app.include_router(router_chat)
app.include_router(router_user)
