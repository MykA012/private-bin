from uuid import UUID, uuid4
from datetime import datetime, timedelta

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import func

from src.database.base import Base


class Paste(Base):
    title: Mapped[str]
    slug: Mapped[UUID] = mapped_column(default=uuid4, unique=True, index=True)
    content: Mapped[str]

    is_expired: Mapped[bool] = mapped_column(default=False)

    created_at: Mapped[datetime] = mapped_column(
        default=func.now(),
        server_default=func.now(),
    )
    expires_at: Mapped[datetime | None]
    expire_seconds: Mapped[int] = mapped_column(default=3600)

    def __init__(self, **kw):
        super().__init__(**kw)
        if "expire_seconds" in kw:
            self.expires_at = datetime.now() + timedelta(seconds=self.expire_seconds)
