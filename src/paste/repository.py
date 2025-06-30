from uuid import UUID
from typing import AsyncIterator
from contextlib import asynccontextmanager

from sqlalchemy import select

from src.database.base import CRUDBase
from src.database.core import session_factory
from src.paste.models import Paste
from src.paste.schemas import PasteCreate


class PasteRepository(CRUDBase):
    async def create(self, paste_in: PasteCreate) -> Paste:
        paste = Paste(**paste_in.model_dump())

        self.session.add(paste)
        await self._commit()
        await self._refresh(paste)
        return paste

    async def get_paste_by_slug(self, slug: UUID) -> Paste | None:
        stmt = select(Paste).where(Paste.slug == slug)
        result = await self.session.execute(stmt)
        paste = result.scalar_one_or_none()
        return paste


@asynccontextmanager
async def get_paste_repo() -> AsyncIterator[PasteRepository]:
    async with session_factory() as session:
        yield PasteRepository(session)
