import os
import pandas as pd
import dash
from dash import dcc, html
import plotly.express as px
import dash_bootstrap_components as dbc

# Setup
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.title = "Mental Health in Tech Dashboard"

# Folder with Excel sheets named '2016.xlsx', '2017.xlsx', etc.
DATA_FOLDER = "c:\Users\Ehtisham\Downloads\cleaned_mental_health_"
YEARS = [2016, 2017, 2018, 2019, 2020]
data_per_year = {}

# Try loading each year's data
for year in YEARS:
    file_path = os.path.join("c:\Users\Ehtisham\Downloads\cleaned_mental_health_", f"{year}.csv")
    if os.path.exists(file_path):
        df = pd.read_excel(file_path)
        if "sentiment_label" in df.columns:
            data_per_year[year] = df
    else:
        data_per_year[year] = None

# Generate yearly pie charts
def generate_pie(year, df):
    fig = px.pie(df, names="sentiment_label", title=f"Sentiment Breakdown - {year}")
    return dcc.Graph(figure=fig)

# Create sentiment trend dataframe
def generate_trend_df(data_dict):
    trend_data = []
    for year, df in data_dict.items():
        if df is not None:
            counts = df["sentiment_label"].value_counts().to_dict()
            trend_data.append({
                "Year": year,
                "Positive": counts.get("Positive", 0),
                "Neutral": counts.get("Neutral", 0),
                "Negative": counts.get("Negative", 0)
            })
    return pd.DataFrame(trend_data)

trend_df = generate_trend_df(data_per_year)

# Create trend line plot
def generate_trend_chart(df):
    df_melt = df.melt(id_vars="Year", var_name="Sentiment", value_name="Count")
    fig = px.line(df_melt, x="Year", y="Count", color="Sentiment", markers=True,
                  title="Sentiment Trend (2016–2020)")
    return dcc.Graph(figure=fig)

# App layout
app.layout = dbc.Container([
    html.H1("Mental Health in Tech (2016–2020)", className="my-4 text-center"),

    dbc.Row([
        dbc.Col(
            html.Div([
                html.H4(str(year)),
                generate_pie(year, df) if df is not None else html.P("Data not available.")
            ]),
            md=6
        ) for year, df in data_per_year.items()
    ]),

    html.Hr(),

    html.H3("Sentiment Trend Across Years", className="my-3"),
    generate_trend_chart(trend_df)
], fluid=True)

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
