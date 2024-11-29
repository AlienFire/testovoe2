from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

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
        return LibraryOut.model_validate_list(objs=objects)
        #return object

    