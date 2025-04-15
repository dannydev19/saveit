from models.model import Base
from models.expense import Expense
from models.fixed_expense import FixedExpense
from models.monthly_fixed_expense import MonthlyFixedExpense
from db.db import engine

Base.metadata.create_all(engine)

import pandas as pd
import streamlit as st

data = {
    "Month": [
        "Jan",
        "Feb",
        "Mar",
        "Apr",
        "May",
        "Jun",
        "Jul",
        "Aug",
        "Sep",
        "Oct",
        "Nov",
        "Dec",
    ],
    "Fixed Expenses": [
        1200,
        1200,
        1200,
        1200,
        1200,
        1200,
        1200,
        1200,
        1200,
        1200,
        1200,
        1200,
    ],
    "Variable Expenses": [300, 350, 400, 380, 420, 450, 480, 500, 530, 550, 580, 600],
}

chart_data = pd.DataFrame(data)
print(f"{chart_data=}")

chart_data.set_index("Month", inplace=True)
print(f"{chart_data=}")

st.title("Fixed vs Variable Expenses")
st.bar_chart(chart_data)
