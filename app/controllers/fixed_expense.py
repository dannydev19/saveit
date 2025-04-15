from controllers.controller import Controller
from models.fixed_expense import FixedExpense
from db.db import session


class FixedExpenseController(Controller):
    @classmethod
    def list_fixed_expenses(cls):
        return session.query(FixedExpense).all()

    @classmethod
    def get_fixed_expense(cls, filter_by: dict = {}):
        return session.query(FixedExpense).filter_by(filter_by).first()
