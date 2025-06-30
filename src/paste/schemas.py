from uuid import UUID
from datetime import datetime

from pydantic import BaseModel


class PasteBase(BaseModel):
    title: str
    content: str
    expire_seconds: int


class PasteCreate(PasteBase):
    ...


class PasteIDB(PasteBase):
    slug: UUID
    is_expired: bool
    created_at: datetime
    expires_at: datetime
