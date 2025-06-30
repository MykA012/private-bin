from uuid import UUID

from fastapi import APIRouter, Depends

from src.paste.deps import paste_by_slug
from src.paste.repository import get_paste_repo
from src.paste.schemas import PasteCreate, PasteIDB

router = APIRouter(tags=["Paste"])


@router.post("/")
async def create_paste(paste_in: PasteCreate) -> PasteIDB:
    async with get_paste_repo() as paste_repo:
        paste = await paste_repo.create(paste_in)
        return paste


@router.get("/paste/{slug}")
async def get_paste(
    paste: UUID = Depends(paste_by_slug),
) -> PasteIDB:
    return paste
