from fastapi import APIRouter
from .library import library_router

root_router = APIRouter()


@root_router.get("/")
async def hello():
    return {"message": "Hello"}

root_router.include_router(
    library_router,
    prefix="/library",
)