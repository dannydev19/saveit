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

index = datetime.now().month - 1

selected_month = st.selectbox("Select a month", months, index=index)

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
    ProjectionExpression="Id, TimeScope, description, price",
)

items, d = [], []

for item in response["Items"]:
    _item = {}
    d.append((item["Id"]["S"], item["TimeScope"]["S"]))

    for k, v in item.items():
        if k in ("Id",):
            continue

        v_type = next(iter(v.keys()))
        v_value = next(iter(v.values()))

        if v_type == "N":
            v_value = float(v_value)

        if k == "TimeScope":
            k = "date"
            v_value = datetime.strptime(v_value.replace("DATE#", ""), "%Y-%m-%d").date()

        _item[k] = v_value

    items.append(_item)


df = pd.DataFrame(items)

column_config = {
    "description": st.column_config.TextColumn(width="large"),
    "price": st.column_config.NumberColumn(width="medium"),
    "date": st.column_config.DateColumn(width="medium"),
}

edited_df = st.data_editor(df, column_config=column_config)

if st.button("Submit changes"):

    for idx, row in enumerate(edited_df.to_dict(orient="records")):

        response = client.update_item(
            TableName="saveit",
            Key={"Id": {"S": d[idx][0]}, "TimeScope": {"S": d[idx][1]}},
            UpdateExpression="SET description = :desc, price = :price",
            ExpressionAttributeValues={
                ":desc": {"S": row["description"]},
                ":price": {"N": str(row["price"])},
            },
            ReturnValues="ALL_NEW",
        )

    st.success(f"Changes submitted!")
