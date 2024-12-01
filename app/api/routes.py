from fastapi import APIRouter
from .library import library_router

root_router = APIRouter()


root_router.include_router(
    library_router,
    prefix="/library",
)