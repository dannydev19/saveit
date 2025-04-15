import streamlit as st
import pandas as pd

from controllers.monthly_fixed_expense import MonthlyFixedExpenseController

st.title("All my monthly fixed expenses")

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

expenses = MonthlyFixedExpenseController.list_by_month(2025, selected_month_number)

df = pd.DataFrame(expenses)

df
