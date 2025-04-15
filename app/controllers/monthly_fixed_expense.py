from sqlalchemy.orm import aliased

from controllers.controller import Controller
from models.monthly_fixed_expense import MonthlyFixedExpense
from models.fixed_expense import FixedExpense
from db.db import session


class MonthlyFixedExpenseController(Controller):
    @classmethod
    def list(cls, filter_by: dict = {}):
        return session.query(MonthlyFixedExpense).filter_by(**filter_by).all()

    @classmethod
    def list_by_month(cls, year: int, month: int):
        fixed_expense_alias = aliased(FixedExpense)
        results = (
            session.query(MonthlyFixedExpense, fixed_expense_alias)
            .join(
                fixed_expense_alias,
                MonthlyFixedExpense.fixed_expense_id == fixed_expense_alias.id,
            )
            .filter(MonthlyFixedExpense.year == year)
            .filter(MonthlyFixedExpense.month == month)
            .all()
        )

        return [
            {
                **fixed_expense.to_json(),
                **monthly_expense.to_json(),
            }
            for monthly_expense, fixed_expense in results
        ]
