import streamlit as st
import pandas as pd

from controllers.expense import ExpenseController

st.title("All my expenses by month")

months = (
    "January 2025",
    "February 2025",
    "March 2025",
    "April 2025",
    "May 2025",
    "June 2025",
    "July 2025",
    "August 2025",
    "September 2025",
    "October 2025",
    "November 2025",
    "December 2025",
)

selected_month = st.selectbox("Select a month", months, index=3)

month_mapping = {month: idx + 1 for idx, month in enumerate(months)}

selected_month_number = month_mapping[selected_month]

expenses = ExpenseController.list_expenses(selected_month_number)
expenses_data = [expense.to_json() for expense in expenses]

df = pd.DataFrame(expenses_data)

df
