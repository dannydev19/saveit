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

chart_data.set_index("Month", inplace=True)

st.title("Fixed vs Variable Expenses")
st.bar_chart(chart_data)
