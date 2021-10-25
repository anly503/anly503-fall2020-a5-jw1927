import pandas as pd
import altair as alt

df = pd.read_csv("household.csv", index_col=None, header=0)
df = df.groupby(["householdID","appliance"], as_index=False).agg({"consumption": "sum"})

chart = alt.Chart(df, title="Bar charts of power consumption of different households").mark_bar().encode(
    x="appliance", y=alt.Y("sum(consumption):Q", axis=alt.Axis(title="Power Consumption")),
    color="appliance:N", column="householdID:N",
).properties(width=250).configure_title(fontSize=24, offset=15, orient="top", anchor="middle")

chart.save("altair.html")
