from sqlalchemy import String, Boolean, Integer, Date
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
import datetime

from models.model import Base
from db.db import engine


class MonthlyFixedExpense(Base):
    __tablename__ = "monthly_fixed_expenses"

    id: Mapped[int] = mapped_column(primary_key=True)
    fixed_expense_id: Mapped[int] = mapped_column(Integer)
    paid: Mapped[bool] = mapped_column(Boolean, default=False)
    year: Mapped[int] = mapped_column(Integer)
    month: Mapped[int] = mapped_column(Integer)
    notes: Mapped[str] = mapped_column(String, default="")

    def to_json(self):
        return {
            "paid": bool(self.paid),
            "notes": self.notes,
        }


Base.metadata.create_all(engine)
