from datetime import datetime

from app import app, db
from sqlalchemy import Text, String, DateTime
from sqlalchemy.orm import Mapped, mapped_column

class Post(db.Model):
    __tablename__ = "posts"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(250))
    content: Mapped[str] = mapped_column(Text)

    created: Mapped[datetime] = mapped_column(DateTime, default=datetime.now())
    update: Mapped[datetime] = mapped_column(DateTime, default=datetime.now(), onupdate=datetime.now())

    user: Mapped[str] = mapped_column(String(25), default="Anonimus")

    def __str__(self):
        return f"Post {self.id}: {self.title}"

