import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc, Input, Output

spacex_df = pd.read_csv("spacex_launch_dash.csv")
app = Dash(__name__)

sites = sorted(spacex_df["Launch Site"].unique())

app.layout = html.Div([
    html.H1("SpaceX Launch Records Dashboard",
            style={"textAlign": "center"}),

    dcc.Dropdown(
        id="site-dropdown",
        options=[{"label": "All Sites", "value": "ALL"}] +
                [{"label": s, "value": s} for s in sites],
        value="ALL",
        placeholder="Select a Launch Site",
        searchable=True
    ),

    dcc.Graph(id="success-pie-chart"),

    html.P("Payload Mass (kg)"),

    dcc.RangeSlider(
        id="payload-slider",
        min=0, max=10000, step=1000,
        value=[0, 10000]
    ),

    dcc.Graph(id="success-payload-scatter-chart")
])

@app.callback(
    Output("success-pie-chart", "figure"),
    Input("site-dropdown", "value")
)
def update_pie(site):
    if site == "ALL":
        data = spacex_df.groupby("Launch Site")["class"].sum().reset_index()
        return px.pie(data, values="class", names="Launch Site",
                      title="Successful Launches by Site")

    data = spacex_df[spacex_df["Launch Site"] == site]
    counts = data["class"].value_counts().reindex([0, 1], fill_value=0)

    return px.pie(
        names=["Failure", "Success"],
        values=counts.values,
        title=f"Launch Outcomes — {site}"
    )

@app.callback(
    Output("success-payload-scatter-chart", "figure"),
    Input("site-dropdown", "value"),
    Input("payload-slider", "value")
)
def update_scatter(site, payload):
    data = spacex_df[
        spacex_df["Payload Mass (kg)"].between(*payload)
    ]

    if site != "ALL":
        data = data[data["Launch Site"] == site]

    return px.scatter(
        data,
        x="Payload Mass (kg)",
        y="class",
        color="Booster Version Category",
        title="Payload Mass vs. Launch Outcome"
    )

if __name__ == "__main__":
    app.run(debug=True, port=8050)