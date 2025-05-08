import streamlit as st
import pandas as pd
from datetime import datetime

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
        ":prefix": {"S": "MONTHLY_FIXED_EXPENSE#"},
        ":datePrefix": {"S": f"YEAR-MONTH#2025-{selected_month_number}"},
    },
    ProjectionExpression="Id, TimeScope, description, paid, price",
)

items = []

for item in response["Items"]:
    _item = {}
    for k, v in item.items():
        v_type = next(iter(v.keys()))
        v_value = next(iter(v.values()))

        if k == "paid":
            v_value = bool(v_value)

        if k == "price":
            v_value = float(v_value)

        _item[k] = v_value

    items.append(_item)


df = pd.DataFrame(items)

column_config = {
    "Id": st.column_config.TextColumn(width="small"),
    "TimeScope": st.column_config.TextColumn(width="small"),
    "description": st.column_config.TextColumn(width="large"),
    "price": st.column_config.NumberColumn(width="medium"),
    "paid": st.column_config.CheckboxColumn(),
}

edited_df = st.data_editor(df, column_config=column_config)

if st.button("Submit changes"):

    for row in edited_df.to_dict(orient="records"):

        response = client.update_item(
            TableName="saveit",
            Key={"Id": {"S": row["Id"]}, "TimeScope": {"S": row["TimeScope"]}},
            UpdateExpression="SET description = :desc, price = :price, paid = :paid",
            ExpressionAttributeValues={
                ":desc": {"S": row["description"]},
                ":price": {"N": str(row["price"])},
                ":paid": {"BOOL": row["paid"]},
            },
            ReturnValues="ALL_NEW",
        )

    st.success(f"Changes submitted!")
