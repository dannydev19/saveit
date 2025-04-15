import datetime
from sqlalchemy import extract

from controllers.controller import Controller
from models.expense import Expense
from db.db import session


class ExpenseController(Controller):
    @classmethod
    def create_expense(
        cls,
        price: float,
        description: str,
        date: datetime.date,
        category: str,
    ):
        session.add(
            Expense(price=price, description=description, date=date, category=category)
        )
        session.commit()

    @classmethod
    def list_expenses(cls, selected_month: int):
        return (
            session.query(Expense)
            .filter(extract("year", Expense.date) == 2025)
            .filter(extract("month", Expense.date) == selected_month)
            .all()
        )
