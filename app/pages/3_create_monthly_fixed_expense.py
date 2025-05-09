import streamlit as st
from uuid import uuid4

from dynamo.db import client

st.title("Create monthly fixed expense")


with st.form("add_monthly_fixed_expense_form"):
    month = st.number_input("Month", min_value=1, step=1, max_value=12)
    description = st.text_input("Description")
    paid = st.checkbox("Paid")
    price = st.number_input("Price", min_value=0.0, step=1.0)
    submit_button = st.form_submit_button("Add Monthly Fixed Expense")

month = str(month) if month > 10 else f"0{month}"

if submit_button:
    client.put_item(
        TableName="saveit",
        Item={
            "Id": {"S": f"MONTHLY_FIXED_EXPENSE#{str(uuid4())}"},
            "TimeScope": {"S": f"YEAR-MONTH#2025-{month}"},
            "description": {"S": description},
            "paid": {"BOOL": paid},
            "price": {"N": str(price)},
        },
    )
    st.success(f"Monthly Fixed Expense added successfully!")
