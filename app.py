from dash import Dash, dcc, html, dash_table
from dash.dependencies import Input, Output, State
import plotly.express as px
import pandas as pd
import requests

API_URL = "http://127.0.0.1:8000/courses/"

COLOR_MAP = {
    1: "#636EFA",
    2: "#00CC96",
    3: "#AB63FA",
    4: "#FFA15A",
    5: "#EF553B",
}

def get_data():
    r = requests.get(API_URL)
    if r.status_code == 200:
        return pd.DataFrame(r.json())
    return pd.DataFrame()

def update_instructor(course_id, instructor):
    requests.put(
        f"{API_URL}{course_id}",
        json={"instructor": instructor}
    )

app = Dash(__name__)

app.layout = html.Div(
    style={"backgroundColor": "#ECEFF1", "padding": "25px"},
    children=[

        html.H1(
            "University Courses Dashboard",
            style={"textAlign": "center", "fontWeight": "bold"},
        ),

        dcc.Interval(id="interval", interval=5000, n_intervals=0),

        # -------- FILTERS --------
        html.Div(
            style={"display": "flex", "gap": "20px", "justifyContent": "center"},
            children=[
                dcc.Dropdown(
                    id="instructor_filter",
                    placeholder="Select Instructor",
                    style={"width": "320px"},
                ),
                dcc.Dropdown(
                    id="course_filter",
                    placeholder="Select Course (Highlight)",
                    style={"width": "320px"},
                ),
            ],
        ),

        html.Br(),

        # -------- BAR CHART --------
        html.Div(
            style={"backgroundColor": "white", "padding": "20px", "borderRadius": "10px"},
            children=[
                html.H3("Credits per Course", style={"fontWeight": "bold"}),
                dcc.Graph(id="bar_chart"),
            ],
        ),

        html.Br(),

        # -------- PIE CHART --------
        html.Div(
            style={"backgroundColor": "white", "padding": "20px", "borderRadius": "10px"},
            children=[
                html.H3("Credit Distribution", style={"fontWeight": "bold"}),
                dcc.Graph(id="pie_chart"),
            ],
        ),

        html.Br(),

        # -------- EDITABLE TABLE --------
        html.Div(
            style={"backgroundColor": "white", "padding": "20px", "borderRadius": "10px"},
            children=[
                html.H3("Instructor Details", style={"fontWeight": "bold"}),
                dash_table.DataTable(
                    id="course_table",
                    editable=True,
                    page_size=8,
                    style_header={"fontWeight": "bold"},
                    style_cell={"padding": "8px"},
                ),
            ],
        ),
    ],
)

# ---------- MAIN DASHBOARD UPDATE ----------
@app.callback(
    [
        Output("bar_chart", "figure"),
        Output("pie_chart", "figure"),
        Output("course_table", "data"),
        Output("course_table", "columns"),
        Output("instructor_filter", "options"),
        Output("course_filter", "options"),
    ],
    [
        Input("interval", "n_intervals"),
        Input("instructor_filter", "value"),
        Input("course_filter", "value"),
    ],
)
def update_dashboard(n, instructor, selected_course):
    df = get_data()

    if instructor:
        df = df[df["instructor"] == instructor]

    bar_fig = px.bar(
        df,
        x="course_name",
        y="credits",
        color="credits",
        color_discrete_map=COLOR_MAP,
    )

    if selected_course:
        bar_fig.update_traces(
            marker_opacity=[
                1 if c == selected_course else 0.4
                for c in df["course_name"]
            ]
        )

    pie_fig = px.pie(
        df,
        names="credits",
        color="credits",
        color_discrete_map=COLOR_MAP,
    )

    table_columns = [
        {"name": col, "id": col, "editable": col == "instructor"}
        for col in df.columns
    ]

    instructor_options = [
        {"label": i, "value": i}
        for i in sorted(get_data()["instructor"].unique())
    ]

    course_options = [
        {"label": c, "value": c}
        for c in df["course_name"].unique()
    ]

    return (
        bar_fig,
        pie_fig,
        df.to_dict("records"),
        table_columns,
        instructor_options,
        course_options,
    )

# ---------- SAVE EDITED INSTRUCTOR ----------
@app.callback(
    Output("interval", "n_intervals"),
    Input("course_table", "data_timestamp"),
    State("course_table", "data"),
)
def save_table_changes(ts, rows):
    if ts is None:
        return 0

    df = pd.DataFrame(rows)
    for _, row in df.iterrows():
        update_instructor(row["id"], row["instructor"])

    return 0

if __name__ == "__main__":
    print("Running Dash on http://127.0.0.1:8050")
    app.run(debug=True, port=8050)