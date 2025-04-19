import streamlit as st
import pandas as pd

from dynamo.db import client

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
        ":prefix": {"S": "MONTHLY_FIXED_EXPENSE#"},
        ":datePrefix": {"S": f"YEAR-MONTH#2025-{selected_month_number}"},
    },
    ProjectionExpression="description, paid",
)

items = []

for item in response["Items"]:
    _item = {}
    for k, v in item.items():
        v_type = next(iter(v.keys()))
        v_value = next(iter(v.values()))

        if k == "paid":
            v_value = bool(v_value)

        _item[k] = v_value

    items.append(_item)


df = pd.DataFrame(items)

df
