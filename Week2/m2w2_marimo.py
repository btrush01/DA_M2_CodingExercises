import marimo

app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import pandas as pd
    import matplotlib.pyplot as plt
    return mo, pd, plt


@app.cell
def _(mo):
    mo.md("""
# Week 2 Quiz: Data Visualization

## Starter Code (RUN THIS FIRST IN YOUR OWN ENVIRONMENT)

```python
import pandas as pd
import matplotlib.pyplot as plt

data = {
    "genre": [
        "Pop","Rock","Hip-Hop","Electronic","Pop","Rock","Hip-Hop","Electronic",
        "Pop","Rock","Hip-Hop","Electronic","Pop","Rock","Hip-Hop","Electronic",
        "Pop","Rock","Hip-Hop","Electronic"
    ],
    "streams": [
        120,90,150,70,130,95,140,80,
        110,85,155,75,125,100,145,78,
        118,92,160,82
    ],
    "likes": [
        30,20,50,15,35,22,48,18,
        28,19,55,16,32,25,47,17,
        29,21,60,19
    ],
    "shares": [
        10,8,20,5,12,9,18,6,
        9,7,22,5,11,10,19,6,
        10,8,25,7
    ],
    "year": [
        2020,2020,2020,2020,2021,2021,2021,2021,
        2022,2022,2022,2022,2023,2023,2023,2023,
        2024,2024,2024,2024
    ]
}

df = pd.DataFrame(data)
```
""")


@app.cell
def _(pd):
    data = {
        "genre": [
            "Pop","Rock","Hip-Hop","Electronic","Pop","Rock","Hip-Hop","Electronic",
            "Pop","Rock","Hip-Hop","Electronic","Pop","Rock","Hip-Hop","Electronic",
            "Pop","Rock","Hip-Hop","Electronic"
        ],
        "streams": [
            120,90,150,70,130,95,140,80,
            110,85,155,75,125,100,145,78,
            118,92,160,82
        ],
        "likes": [
            30,20,50,15,35,22,48,18,
            28,19,55,16,32,25,47,17,
            29,21,60,19
        ],
        "shares": [
            10,8,20,5,12,9,18,6,
            9,7,22,5,11,10,19,6,
            10,8,25,7
        ],
        "year": [
            2020,2020,2020,2020,2021,2021,2021,2021,
            2022,2022,2022,2022,2023,2023,2023,2023,
            2024,2024,2024,2024
        ]
    }
    df = pd.DataFrame(data)
    return df


@app.cell
def _(mo):
    mo.md("""## 1. Create a Bar Plot

- x-axis: genre  
- y-axis: streams  
- title: Streams by Genre  
""")


@app.cell
def _(mo):
    bar_show = mo.ui.checkbox(label="Show expected output", value=False)
    bar_show
    return bar_show


@app.cell
def _(df, mo, plt, bar_show):
    bar_output = None
    if bar_show.value:
        _fig_bar, _ax_bar = plt.subplots()
        df.groupby("genre")["streams"].mean().plot(kind="bar", ax=_ax_bar)
        _ax_bar.set_xlabel("genre")
        _ax_bar.set_ylabel("streams")
        _ax_bar.set_title("Streams by Genre")
        bar_output = mo.vstack([mo.md("Expected output"), _fig_bar])
    bar_output


@app.cell
def _(mo):
    mo.md("""## 2. Create a Scatter Plot

- x-axis: likes  
- y-axis: streams  
- title: Streams vs Likes  
""")


@app.cell
def _(mo):
    scatter_show = mo.ui.checkbox(label="Show expected output", value=False)
    scatter_show
    return scatter_show


@app.cell
def _(df, mo, plt, scatter_show):
    scatter_output = None
    if scatter_show.value:
        _fig_scatter, _ax_scatter = plt.subplots()
        _ax_scatter.scatter(df["likes"], df["streams"])
        _ax_scatter.set_xlabel("likes")
        _ax_scatter.set_ylabel("streams")
        _ax_scatter.set_title("Streams vs Likes")
        scatter_output = mo.vstack([mo.md("Expected output"), _fig_scatter])
    scatter_output


@app.cell
def _(mo):
    mo.md("""## 3. Create a Histogram

- Use streams column  
- title: Streams Distribution  
""")


@app.cell
def _(mo):
    hist_show = mo.ui.checkbox(label="Show expected output", value=False)
    hist_show
    return hist_show


@app.cell
def _(df, mo, plt, hist_show):
    hist_output = None
    if hist_show.value:
        _fig_hist, _ax_hist = plt.subplots()
        _ax_hist.hist(df["streams"])
        _ax_hist.set_title("Streams Distribution")
        hist_output = mo.vstack([mo.md("Expected output"), _fig_hist])
    hist_output


if __name__ == "__main__":
    app.run()
