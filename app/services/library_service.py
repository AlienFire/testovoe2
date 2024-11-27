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
        library: Library
    ) -> LibraryOut:
        self._session.add(library)
        await self._session.commit()
        return LibraryOut.model_validate(obj=library)

    async def get_all(self) -> list[LibraryOut]:
        stmt = select(Library)
        object = (await self._session.scalars(stmt)).all()
        return LibraryOut.model_validate(obj=object)
