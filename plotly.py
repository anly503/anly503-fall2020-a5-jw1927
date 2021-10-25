import pandas as pd
import plotly.express as px

df = pd.read_csv("household.csv", index_col=None, header=0)

fig = px.line(data_frame=df, x="time", y="consumption",
      color="appliance", facet_col="householdID", facet_col_wrap=3,
      labels={"consumption": "Power Consumption"},
      title="Power consumption of differnet appliances during time",
      width=1000,
      height=500).update_layout(title={
        "text": "Power consumption of differnet appliances during time",
        "y": 0.9,
        "x": 0.5,
        "xanchor": "center",
        "yanchor": "top"}, showlegend=False)

fig.write_html("plotly.html")
