from sqlalchemy import Integer, String, Enum

from sqlalchemy.orm import declarative_base, Mapped, mapped_column

from app.contracts import StatusBookEnum

Base = declarative_base()


class Library(Base):
    __tablename__ = "library"
    id: Mapped[int] = mapped_column(
        "id",
        Integer,
        primary_key=True,
    )
    title: Mapped[str] = mapped_column(
        "title",
        String(300),
        unique=True,
    )
    author: Mapped[str] = mapped_column(
        "author",
        String(300),
    )
    year: Mapped[str] = mapped_column(
        "year",
        Integer,
    )
    status: Mapped[StatusBookEnum] = mapped_column(
        Enum(StatusBookEnum, nattive_enam=False, length=100),
        server_default=StatusBookEnum.available,
    )