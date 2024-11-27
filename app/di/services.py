from typing import TypeVar

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.di.datebase import get_session
from app.services.library_service import LibraryService

ServiceT = TypeVar("ServiceT")


def get_service(
    service: type[ServiceT],
):
    def create_service(
        session=Depends(get_session),
    ) -> ServiceT:
        return service(session=session)

    return Depends(create_service)


def get_library_service(session=Depends(get_session)) -> LibraryService:

    return LibraryService(session=session)