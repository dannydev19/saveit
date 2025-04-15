import streamlit as st

from controllers.expense import ExpenseController
from enums import FixedExpensesEnum, CategoryExpenseEnum

st.title("Create expense")

fixed_expenses = FixedExpensesEnum.get_values()
category_expenses = CategoryExpenseEnum.get_values()


with st.form("add_expense_form"):
    price = st.number_input("Price", min_value=0.0, step=0.1)
    description = st.text_input("Description")
    when = st.date_input("Date", value="today")
    category_expense = st.selectbox("Category", category_expenses)
    submit_button = st.form_submit_button("Add Expense")


if submit_button:
    ExpenseController.create_expense(price, description, when, category_expense)
    st.success(f"Expense added successfully!")
