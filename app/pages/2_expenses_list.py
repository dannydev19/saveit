import streamlit as st
import pandas as pd
from datetime import datetime

from dynamo.db import client


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

selected_month_number = (
    str(selected_month_number)
    if selected_month_number > 10
    else f"0{selected_month_number}"
)

response = client.scan(
    TableName="saveit",
    FilterExpression="begins_with(#id, :prefix) AND begins_with(#sk, :datePrefix)",
    ExpressionAttributeNames={
        "#id": "Id",
        "#sk": "TimeScope",
    },
    ExpressionAttributeValues={
        ":prefix": {"S": "EXPENSE#"},
        ":datePrefix": {"S": f"DATE#2025-{selected_month_number}"},
    },
    ProjectionExpression="TimeScope, description, price",
)

items = []

for item in response["Items"]:
    _item = {}
    for k, v in item.items():
        v_type = next(iter(v.keys()))
        v_value = next(iter(v.values()))

        if v_type == "N":
            v_value = float(v_value)

        if k == "TimeScope":
            k = "date"
            v_value = datetime.strptime(v_value.replace("DATE#", ""), "%Y-%m-%d")

        _item[k] = v_value

    items.append(_item)


df = pd.DataFrame(items)

df
