import datetime
from sqlalchemy import String, Float, Date, Boolean, Integer
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from models.model import Base
from db.db import engine
from enums import CategoryExpenseEnum


class Expense(Base):
    __tablename__ = "expenses"

    id: Mapped[int] = mapped_column(primary_key=True)
    price: Mapped[float] = mapped_column(Float)
    description: Mapped[str] = mapped_column(String, default="")
    category: Mapped[str] = mapped_column(
        String, default=CategoryExpenseEnum.OTHERS.value
    )
    date: Mapped[datetime.date] = mapped_column(Date)

    def to_json(self):
        return {
            "price": self.price,
            "description": self.description,
            "category": self.category,
            "date": self.date.isoformat(),
        }


Base.metadata.create_all(engine)
