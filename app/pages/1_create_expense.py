import streamlit as st

from dynamo.db import client
from enums import FixedExpensesEnum, CategoryExpenseEnum

st.title("Create expense")

fixed_expenses = FixedExpensesEnum.get_values()
category_expenses = CategoryExpenseEnum.get_values()


with st.form("add_expense_form"):
    id = st.number_input("Id", value=1, step=1)
    price = st.number_input("Price", min_value=0.0, step=1.0)
    description = st.text_input("Description")
    when = st.date_input("Date", value="today")
    category_expense = st.selectbox("Category", category_expenses)
    submit_button = st.form_submit_button("Add Expense")


if submit_button:
    client.put_item(
        TableName="saveit",
        Item={
            "Id": {"S": f"EXPENSE#{id}"},
            "TimeScope": {"S": f"DATE#{when.strftime("%Y-%m-%d")}"},
            "description": {"S": description},
            "price": {"N": str(price)},
        },
    )
    st.success(f"Expense added successfully!")
