from typing import Annotated
from uuid import UUID

from fastapi import Path, HTTPException

from src.paste.repository import get_paste_repo


async def paste_by_slug(slug: Annotated[UUID, Path]):
    async with get_paste_repo() as paste_repo:
        paste = await paste_repo.get_paste_by_slug(slug=slug)

        if not paste:
            raise HTTPException(404)
        return paste
