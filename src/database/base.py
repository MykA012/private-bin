from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import DeclarativeBase, declared_attr
from sqlalchemy.orm import Mapped, mapped_column


class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key=True)

    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower() + "s"


class CRUDBase:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def _commit(self) -> None:
        await self.session.commit()

    async def _refresh(self, item):
        await self.session.refresh(item)
