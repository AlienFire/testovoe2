from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.contracts import StatusBookEnum
from app.db.models import Library
from app.schema import (
    LibraryInput,
    LibraryOut
)


class LibraryService:
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def create_book(
        self,
        title: str,
        author: str,
        year: int,
        #library: Library
    ) -> Library:
        object = Library(
            title=title,
            author=author,
            year=year,
            )
        self._session.add(object)
        await self._session.commit()
        return object

    async def get_all(self) -> Library:
        stmt = select(Library)
        objects = (await self._session.scalars(stmt)).all()
        return LibraryOut.model_validate(obj=objects)

    async def get_book_by_id(
        self,
        id,
    ) -> Library | None:
        book = await self._session.get(Library, ident=id)
        if book is None:
            raise HTTPException(
                status_code=404,
                detail=f"Book with id={id} is not found",
                )
        return book

    async def delete_book(
        self,
        id: int,
    ) -> None:
        book = await self.get_book_by_id(id=id)
        await self._session.delete(book)
        await self._session.commit()
        return None

    async def get_book(
        self,
        title: str | None,
        author: str | None,
        year: int | None,
    ) -> list[LibraryOut]:
        title_query = ""
        author_query = ""

        if title is not None:
            title_query = title
        if author is not None:
            author_query = author
        if year is not None:
            stmt = select(Library).where(
                Library.author == author_query
                or Library.title == title_query
                or Library.year == year)
            objects = (await self._session.scalars(stmt)).all()
        else:
            stmt = select(Library).where(
                Library.author == author_query
                or Library.title == title_query)
            objects = (await self._session.scalars(stmt)).all()
        return LibraryOut.model_validate(obj=objects)

    async def update_book(
        self,
        id: int,
        stutus: StatusBookEnum,
    ) -> Library:
        book = await self.get_book_by_id(id=id)
        book.status = stutus
        self._session.add(book)
        await self._session.commit()
        return book