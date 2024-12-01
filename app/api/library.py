from fastapi import APIRouter, Depends, status

from app.contracts import  StatusBookEnum
from app.schema import LibraryInput, LibraryOut
from app.di.services import get_library_service
from app.services.library_service import LibraryService

library_router = APIRouter()


@library_router.get("/",
                    description="You can get all books",
                    )
async def get_all_books(
    services: LibraryService = Depends(get_library_service),

) -> list[LibraryOut]:
    object = await services.get_all()
    return object


@library_router.post("/book", description="You can add new book")
async def create_book(
    book_data: LibraryInput,
    services: LibraryService = Depends(get_library_service),
) -> LibraryOut:
    new_book = await services.create_book(
        title=book_data.title,
        author=book_data.author,
        year=book_data.year,
    )
    return LibraryOut.model_validate(new_book, from_attributes=True)


@library_router.delete(
    "/{id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_book(
    id: int,
    service: LibraryService = Depends(get_library_service),
) -> None:
    await service.delete_book(id=id)
    return None


@library_router.get("/",
                    description="You can find the book by title, author or year",
                    )
async def get_book(
    title: str | None,
    author: str | None,
    year: int | None,
    service: LibraryService = Depends(get_library_service),
) -> list[LibraryOut]:
    books = await service.get_book(
        title=title,
        author=author,
        year=year,
        )
    return books



@library_router.put(
    "/{id}",
    description="You can change the status of book"
)
async def change_status_of_book(
    id: int,
    status: StatusBookEnum,
    service: LibraryService = Depends(get_library_service),
) -> LibraryOut:

    update_book = await service.update_book(
        id=id,
        stutus=status,
    )
    return LibraryOut.model_validate(update_book, from_attributes=True)
