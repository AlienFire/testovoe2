from fastapi import APIRouter, Depends, status

from app.schema import LibraryInput, LibraryOut
from app.di.services import get_library_service
from app.services.library_service import LibraryService

library_router = APIRouter()


@library_router.get("/")
async def get_all_books(
    services: LibraryService = Depends(get_library_service),

) -> list[LibraryOut]:
    object = await services.get_all()
    return LibraryOut.model_validate(object)


@library_router.post("/book")
async def create_book(
    book_data: LibraryInput,
    services: LibraryService = Depends(get_library_service),
) -> LibraryOut:

    return await services.create_book(
        title=book_data.title,
        autor=book_data.author,
        year=book_data.year,
    )