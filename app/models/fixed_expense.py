from sqlalchemy import String, Float
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from models.model import Base
from db.db import engine


class FixedExpense(Base):
    __tablename__ = "fixed_expenses"

    id: Mapped[int] = mapped_column(primary_key=True)
    price: Mapped[float] = mapped_column(Float, nullable=True)
    description: Mapped[str] = mapped_column(String, default="")
    periodicity: Mapped[str] = mapped_column(String, nullable=True)

    def to_json(self):
        return {
            "description": self.description,
            "price": self.price,
        }


Base.metadata.create_all(engine)
