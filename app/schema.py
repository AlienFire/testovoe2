from typing import Self, TypeVar
from collections.abc import Sequence
from pydantic import BaseModel, Field
from app.db.models import Base

DBModelT = TypeVar("DBModelT", bound=Base)


class BaseEntity(BaseModel):
    model_config = {"from_attributes": True}

    @classmethod
    def model_validate_list(cls, objs: Sequence[DBModelT]) -> list[Self]:
        return [cls.model_validate(obj) for obj in objs]


class BaseLibrary(BaseModel):
    """Базовая схема для Library"""

    title: str = Field(..., description="название книги")
    author: str = Field(description="автор книги")
    year: int = Field(description="год издания")


class LibraryInput(BaseLibrary):
    """Схема для создания книг"""

    pass


class LibraryOut(BaseLibrary):
    """Схема вывода книг"""

    id: int
