from fastapi import APIRouter

from src.paste.routes import router as paste_router

root_router = APIRouter()
root_router.include_router(paste_router)
