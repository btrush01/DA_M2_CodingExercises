import marimo

app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import pandas as pd
    import numpy as np
    return mo, pd, np


@app.cell
def _(pd):
    # Section 1, Exercise Set 1 dataset
    data_local = {
        "Name": [
            "Alice", "Bob", "Charlie", "David", "Evelyn",
            "Frank", "Grace", "Henry", "Isla", "Jack",
            "Karen", "Leo", "Mia", "Noah", "Olivia",
            "Paul", "Quinn", "Ruby", "Sam", "Tina"
        ],
        "Age": [25, 32, 37, 29, 41, 28, 34, 45, 26, 31, 39, 27, 33, 36, 30, 42, 24, 38, 35, 29],
        "Department": [
            "HR", "Engineering", "Sales", "Marketing", "Engineering",
            "Finance", "Support", "Operations", "HR", "Sales",
            "Engineering", "Support", "Marketing", "Finance", "Operations",
            "Engineering", "HR", "Sales", "Support", "Marketing"
        ],
        "Salary": [
            50000, 75000, 62000, 58000, 80000,
            54000, 52000, 70000, 51000, 64000,
            82000, 53000, 60000, 56000, 68000,
            79000, 49500, 65500, 54500, 61000
        ],
    }
    df_local = pd.DataFrame(data_local)
    return df_local


@app.cell
def _(pd):
    # Section 1, Exercise Sets 2 and 3 dataset
    titanic_url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
    df_titanic = pd.read_csv(titanic_url)
    return df_titanic, titanic_url


@app.cell
def _(pd):
    # Section 2, Exercise Set 1 dataset
    data_drop = {
        "Name": ["Alice", "Bob", "Charlie", "David"],
        "Age": [25, 30, 35, 40],
        "City": ["NYC", "LA", "Chicago", "Miami"],
        "Email": ["a@example.com", "b@example.com", "c@example.com", "d@example.com"],
    }
    df_drop = pd.DataFrame(data_drop)
    return df_drop


@app.cell
def _(np, pd):
    # Section 2, Exercise Set 2 dataset
    data_missing = {
        "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
        "Age": [25, np.nan, 35, 40, None],
        "City": ["NYC", "LA", None, "Miami", "Boston"],
    }
    df_missing = pd.DataFrame(data_missing)
    return df_missing


@app.cell
def _(pd):
    # Section 2, Exercise Set 3 dataset
    data_duplicates = {
        "Name": ["Alice", "Bob", "Charlie", "Alice", "Bob", "Diana"],
        "Age": [25, 30, 35, 25, 30, 40],
        "City": ["NYC", "LA", "SF", "NYC", "LA", "NYC"],
    }
    df_duplicates = pd.DataFrame(data_duplicates)
    return df_duplicates


@app.cell
def _(pd):
    # Section 3, Exercise Set 1 dataset
    data_rename = {
        "fname": ["Alice", "Bob", "Charlie"],
        "lname": ["Smith", "Jones", "Brown"],
        "ctry": ["USA", "Canada", "UK"],
    }
    df_rename = pd.DataFrame(data_rename)
    return df_rename


@app.cell
def _(pd):
    # Section 3, Exercise Set 2 dataset
    data_reorder = {
        "Name": ["Alice", "Bob", "Charlie"],
        "Dept": ["HR", "Finance", "IT"],
        "Sal": [60000, 70000, 80000],
    }
    df_reorder = pd.DataFrame(data_reorder)
    return df_reorder


@app.cell
def _(pd):
    # Section 3, Exercise Set 3 dataset
    data_group = {
        "Store": ["A", "A", "A", "B", "B", "C", "C", "C", "C"],
        "Product": ["Apples", "Oranges", "Bananas", "Apples", "Bananas", "Oranges", "Apples", "Bananas", "Bananas"],
        "Sales": [100, 80, 90, 120, 110, 60, 95, 85, 75],
        "Profit": [30, 25, 20, 40, 35, 15, 32, 22, 18],
    }
    df_group = pd.DataFrame(data_group)
    return df_group


@app.cell
def _(pd):
    # Section 3, Exercise Set 4 datasets
    df_customers = pd.DataFrame(
        {"CustomerName": ["Alice", "Bob", "Charlie"]},
        index=[101, 102, 103],
    )
    df_orders = pd.DataFrame(
        {"OrderTotal": [250, 300, 400]},
        index=[101, 102, 103],
    )
    df_cities = pd.DataFrame(
        {"City": ["NYC", "LA", "Chicago"]},
        index=[101, 102, 103],
    )
    return df_cities, df_customers, df_orders


@app.cell
def _(mo):
    mo.md(
        """
# Module 2 Coding Exercises: Week 1

## How to use this page
1. Read the prompt for the exercise.
2. Complete the code in your own VS Code file or notebook.
3. Run your code locally.
4. Come back here and reveal the expected output.
5. Compare your result to the expected output.

This app does **not** show the answer code. It only reveals the output your result should match.
"""
    )


@app.cell
def _(mo):
    mo.md(
        """
## Week 1 Sections
- Pandas: A Data Analyst's Best Friend
- Clean & Tidy Data
- Data Wrangling Essentials
"""
    )


@app.cell
def _(mo):
    mo.md(
        """
---
# Section 1: Pandas: A Data Analyst's Best Friend
"""
    )


@app.cell
def _(mo):
    mo.md(
        """
## Exercise Set 1: Viewing Data

Use this starter code in your own environment:

```python
import pandas as pd

data = {
    "Name": [
        "Alice", "Bob", "Charlie", "David", "Evelyn",
        "Frank", "Grace", "Henry", "Isla", "Jack",
        "Karen", "Leo", "Mia", "Noah", "Olivia",
        "Paul", "Quinn", "Ruby", "Sam", "Tina"
    ],
    "Age": [25, 32, 37, 29, 41, 28, 34, 45, 26, 31, 39, 27, 33, 36, 30, 42, 24, 38, 35, 29],
    "Department": [
        "HR", "Engineering", "Sales", "Marketing", "Engineering",
        "Finance", "Support", "Operations", "HR", "Sales",
        "Engineering", "Support", "Marketing", "Finance", "Operations",
        "Engineering", "HR", "Sales", "Support", "Marketing"
    ],
    "Salary": [
        50000, 75000, 62000, 58000, 80000,
        54000, 52000, 70000, 51000, 64000,
        82000, 53000, 60000, 56000, 68000,
        79000, 49500, 65500, 54500, 61000
    ],
}

df = pd.DataFrame(data)
```
"""
    )


@app.cell
def _(mo):
    mo.md(
        """
### Exercise 1

View the first five rows of the DataFrame.
"""
    )


@app.cell
def _(mo):
    view_ex1_show = mo.ui.checkbox(
        label="Show expected output for Viewing Data, Exercise 1",
        value=False,
    )
    view_ex1_show
    return view_ex1_show


@app.cell
def _(df_local, mo, view_ex1_show):
    view_ex1_output = None
    if view_ex1_show.value:
        view_ex1_output = mo.vstack([
            mo.md("### Expected output"),
            df_local.head(),
        ])
    view_ex1_output


@app.cell
def _(mo):
    mo.md(
        """
### Exercise 2

View the last five rows of the DataFrame.
"""
    )


@app.cell
def _(mo):
    view_ex2_show = mo.ui.checkbox(
        label="Show expected output for Viewing Data, Exercise 2",
        value=False,
    )
    view_ex2_show
    return view_ex2_show


@app.cell
def _(df_local, mo, view_ex2_show):
    view_ex2_output = None
    if view_ex2_show.value:
        view_ex2_output = mo.vstack([
            mo.md("### Expected output"),
            df_local.tail(),
        ])
    view_ex2_output


@app.cell
def _(mo):
    mo.md(
        """
### Exercise 3

Get basic info about the DataFrame.
"""
    )


@app.cell
def _(mo):
    view_ex3_show = mo.ui.checkbox(
        label="Show expected output for Viewing Data, Exercise 3",
        value=False,
    )
    view_ex3_show
    return view_ex3_show


@app.cell
def _(df_local, mo, view_ex3_show):
    view_ex3_output = None
    if view_ex3_show.value:
        import io
        import sys

        buffer = io.StringIO()
        old_stdout = sys.stdout
        try:
            sys.stdout = buffer
            df_local.info()
        finally:
            sys.stdout = old_stdout

        view_ex3_output = mo.vstack([
            mo.md("### Expected output"),
            mo.md(f"```\n{buffer.getvalue()}\n```"),
        ])
    view_ex3_output


@app.cell
def _(mo):
    mo.md(
        """
### Exercise 4

Check the shape of the DataFrame.
"""
    )


@app.cell
def _(mo):
    view_ex4_show = mo.ui.checkbox(
        label="Show expected output for Viewing Data, Exercise 4",
        value=False,
    )
    view_ex4_show
    return view_ex4_show


@app.cell
def _(df_local, mo, view_ex4_show):
    view_ex4_output = None
    if view_ex4_show.value:
        view_ex4_output = mo.vstack([
            mo.md("### Expected output"),
            mo.md(f"`{df_local.shape}`"),
        ])
    view_ex4_output


@app.cell
def _(mo, titanic_url):
    mo.md(
        f"""
## Exercise Set 2: Indexing with `.loc[]` and `.iloc[]`

Use this starter code in your own environment:

```python
import pandas as pd

url = "{titanic_url}"
df = pd.read_csv(url)

print(df.head())
```
"""
    )


@app.cell
def _(mo):
    mo.md(
        """
### Exercise 1

Use `.loc` to get the name and age of the passenger with index 12.
"""
    )


@app.cell
def _(mo):
    idx_ex1_show = mo.ui.checkbox(
        label="Show expected output for Indexing, Exercise 1",
        value=False,
    )
    idx_ex1_show
    return idx_ex1_show


@app.cell
def _(df_titanic, mo, idx_ex1_show):
    idx_ex1_output = None
    if idx_ex1_show.value:
        idx_ex1_output = mo.vstack([
            mo.md("### Expected output"),
            df_titanic.loc[12, ["Name", "Age"]],
        ])
    idx_ex1_output


@app.cell
def _(mo):
    mo.md(
        """
### Exercise 2

Use `.iloc` to get the first 5 rows and first 3 columns.
"""
    )


@app.cell
def _(mo):
    idx_ex2_show = mo.ui.checkbox(
        label="Show expected output for Indexing, Exercise 2",
        value=False,
    )
    idx_ex2_show
    return idx_ex2_show


@app.cell
def _(df_titanic, mo, idx_ex2_show):
    idx_ex2_output = None
    if idx_ex2_show.value:
        idx_ex2_output = mo.vstack([
            mo.md("### Expected output"),
            df_titanic.iloc[:5, :3],
        ])
    idx_ex2_output


@app.cell
def _(mo):
    mo.md(
        """
### Exercise 3

Use `.loc` to get all passengers in 1st class who are female.
"""
    )


@app.cell
def _(mo):
    idx_ex3_show = mo.ui.checkbox(
        label="Show expected output for Indexing, Exercise 3",
        value=False,
    )
    idx_ex3_show
    return idx_ex3_show


@app.cell
def _(df_titanic, mo, idx_ex3_show):
    idx_ex3_output = None
    if idx_ex3_show.value:
        idx_ex3_output = mo.vstack([
            mo.md("### Expected output"),
            df_titanic.loc[(df_titanic["Pclass"] == 1) & (df_titanic["Sex"] == "female")],
        ])
    idx_ex3_output


@app.cell
def _(mo):
    mo.md(
        """
### Exercise 4

Use `.iloc` to get the age of the 10th passenger (by position).
"""
    )


@app.cell
def _(mo):
    idx_ex4_show = mo.ui.checkbox(
        label="Show expected output for Indexing, Exercise 4",
        value=False,
    )
    idx_ex4_show
    return idx_ex4_show


@app.cell
def _(df_titanic, mo, idx_ex4_show):
    idx_ex4_output = None
    if idx_ex4_show.value:
        idx_ex4_output = mo.vstack([
            mo.md("### Expected output"),
            mo.md(f"`{df_titanic.iloc[9]['Age']}`"),
        ])
    idx_ex4_output


@app.cell
def _(mo):
    mo.md(
        """
### Exercise 5

Use `.loc` to get the `Fare` and `Survived` values for passengers with index 100 to 105.
"""
    )


@app.cell
def _(mo):
    idx_ex5_show = mo.ui.checkbox(
        label="Show expected output for Indexing, Exercise 5",
        value=False,
    )
    idx_ex5_show
    return idx_ex5_show


@app.cell
def _(df_titanic, mo, idx_ex5_show):
    idx_ex5_output = None
    if idx_ex5_show.value:
        idx_ex5_output = mo.vstack([
            mo.md("### Expected output"),
            df_titanic.loc[100:105, ["Fare", "Survived"]],
        ])
    idx_ex5_output


@app.cell
def _(mo, titanic_url):
    mo.md(
        f"""
## Exercise Set 3: Summary Tools

Use this starter code in your own environment:

```python
import pandas as pd

url = "{titanic_url}"
df = pd.read_csv(url)

df.head()
```
"""
    )


@app.cell
def _(mo):
    mo.md(
        """
### Exercise 1

Summarize the numeric columns.
"""
    )


@app.cell
def _(mo):
    sum_ex1_show = mo.ui.checkbox(
        label="Show expected output for Summary Tools, Exercise 1",
        value=False,
    )
    sum_ex1_show
    return sum_ex1_show


@app.cell
def _(df_titanic, mo, sum_ex1_show):
    sum_ex1_output = None
    if sum_ex1_show.value:
        sum_ex1_output = mo.vstack([
            mo.md("### Expected output"),
            df_titanic.describe(),
        ])
    sum_ex1_output


@app.cell
def _(mo):
    mo.md(
        """
### Exercise 2

Use `.value_counts()` to see counts for embarkation ports.
"""
    )


@app.cell
def _(mo):
    sum_ex2_show = mo.ui.checkbox(
        label="Show expected output for Summary Tools, Exercise 2",
        value=False,
    )
    sum_ex2_show
    return sum_ex2_show


@app.cell
def _(df_titanic, mo, sum_ex2_show):
    sum_ex2_output = None
    if sum_ex2_show.value:
        sum_ex2_output = mo.vstack([
            mo.md("### Expected output"),
            df_titanic["Embarked"].value_counts(),
        ])
    sum_ex2_output


@app.cell
def _(mo):
    mo.md(
        """
### Exercise 3

Use `.value_counts()` to count passenger classes.
"""
    )


@app.cell
def _(mo):
    sum_ex3_show = mo.ui.checkbox(
        label="Show expected output for Summary Tools, Exercise 3",
        value=False,
    )
    sum_ex3_show
    return sum_ex3_show


@app.cell
def _(df_titanic, mo, sum_ex3_show):
    sum_ex3_output = None
    if sum_ex3_show.value:
        sum_ex3_output = mo.vstack([
            mo.md("### Expected output"),
            df_titanic["Pclass"].value_counts(),
        ])
    sum_ex3_output


@app.cell
def _(mo):
    mo.md(
        """
### Exercise 4

Show the average (mean) age of passengers.
"""
    )


@app.cell
def _(mo):
    sum_ex4_show = mo.ui.checkbox(
        label="Show expected output for Summary Tools, Exercise 4",
        value=False,
    )
    sum_ex4_show
    return sum_ex4_show


@app.cell
def _(df_titanic, mo, sum_ex4_show):
    sum_ex4_output = None
    if sum_ex4_show.value:
        sum_ex4_output = mo.vstack([
            mo.md("### Expected output"),
            mo.md(f"`{df_titanic['Age'].mean()}`"),
        ])
    sum_ex4_output


@app.cell
def _(mo):
    mo.md(
        """
### Exercise 5

Show the maximum fare paid.
"""
    )


@app.cell
def _(mo):
    sum_ex5_show = mo.ui.checkbox(
        label="Show expected output for Summary Tools, Exercise 5",
        value=False,
    )
    sum_ex5_show
    return sum_ex5_show


@app.cell
def _(df_titanic, mo, sum_ex5_show):
    sum_ex5_output = None
    if sum_ex5_show.value:
        sum_ex5_output = mo.vstack([
            mo.md("### Expected output"),
            mo.md(f"`{df_titanic['Fare'].max()}`"),
        ])
    sum_ex5_output


@app.cell
def _(mo):
    mo.md(
        """
### Exercise 6

Show how many unique names are in the dataset.
"""
    )


@app.cell
def _(mo):
    sum_ex6_show = mo.ui.checkbox(
        label="Show expected output for Summary Tools, Exercise 6",
        value=False,
    )
    sum_ex6_show
    return sum_ex6_show


@app.cell
def _(df_titanic, mo, sum_ex6_show):
    sum_ex6_output = None
    if sum_ex6_show.value:
        sum_ex6_output = mo.vstack([
            mo.md("### Expected output"),
            mo.md(f"`{df_titanic['Name'].nunique()}`"),
        ])
    sum_ex6_output


@app.cell
def _(mo):
    mo.md(
        """
### Exercise 7

Show counts for values in the `Sex` column.
"""
    )


@app.cell
def _(mo):
    sum_ex7_show = mo.ui.checkbox(
        label="Show expected output for Summary Tools, Exercise 7",
        value=False,
    )
    sum_ex7_show
    return sum_ex7_show


@app.cell
def _(df_titanic, mo, sum_ex7_show):
    sum_ex7_output = None
    if sum_ex7_show.value:
        sum_ex7_output = mo.vstack([
            mo.md("### Expected output"),
            df_titanic["Sex"].value_counts(),
        ])
    sum_ex7_output


@app.cell
def _(mo):
    mo.md(
        """
### Exercise 8

Show how many unique values are in each column.
"""
    )


@app.cell
def _(mo):
    sum_ex8_show = mo.ui.checkbox(
        label="Show expected output for Summary Tools, Exercise 8",
        value=False,
    )
    sum_ex8_show
    return sum_ex8_show


@app.cell
def _(df_titanic, mo, sum_ex8_show):
    sum_ex8_output = None
    if sum_ex8_show.value:
        sum_ex8_output = mo.vstack([
            mo.md("### Expected output"),
            df_titanic.nunique(),
        ])
    sum_ex8_output


@app.cell
def _(mo):
    mo.md(
        """
---
# Section 2: Clean & Tidy Data
"""
    )


@app.cell
def _(mo):
    mo.md(
        """
## Exercise Set 1: Dropping Data

Use this starter code in your own environment:

```python
import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [25, 30, 35, 40],
    "City": ["NYC", "LA", "Chicago", "Miami"],
    "Email": ["a@example.com", "b@example.com", "c@example.com", "d@example.com"],
}

df = pd.DataFrame(data)
```
"""
    )


@app.cell
def _(mo):
    mo.md(
        """
### Exercise 1

Drop the `Email` column and store the result in a new variable.
"""
    )


@app.cell
def _(mo):
    clean_drop_ex1_show = mo.ui.checkbox(
        label="Show expected output for Dropping Data, Exercise 1",
        value=False,
    )
    clean_drop_ex1_show
    return clean_drop_ex1_show


@app.cell
def _(df_drop, mo, clean_drop_ex1_show):
    clean_drop_ex1_output = None
    if clean_drop_ex1_show.value:
        clean_drop_ex1_output = mo.vstack([
            mo.md("### Expected output"),
            df_drop.drop(columns=["Email"]),
        ])
    clean_drop_ex1_output


@app.cell
def _(mo):
    mo.md(
        """
### Exercise 2

Drop the row with index `2` in place.
"""
    )


@app.cell
def _(mo):
    clean_drop_ex2_show = mo.ui.checkbox(
        label="Show expected output for Dropping Data, Exercise 2",
        value=False,
    )
    clean_drop_ex2_show
    return clean_drop_ex2_show


@app.cell
def _(df_drop, mo, clean_drop_ex2_show):
    clean_drop_ex2_output = None
    if clean_drop_ex2_show.value:
        temp_df_drop_2 = df_drop.copy()
        temp_df_drop_2.drop(index=2, inplace=True)
        clean_drop_ex2_output = mo.vstack([
            mo.md("### Expected output"),
            temp_df_drop_2,
        ])
    clean_drop_ex2_output


@app.cell
def _(mo):
    mo.md(
        """
### Exercise 3

Drop the `City` and `Email` columns, and assign the result back to `df`.
"""
    )


@app.cell
def _(mo):
    clean_drop_ex3_show = mo.ui.checkbox(
        label="Show expected output for Dropping Data, Exercise 3",
        value=False,
    )
    clean_drop_ex3_show
    return clean_drop_ex3_show


@app.cell
def _(df_drop, mo, clean_drop_ex3_show):
    clean_drop_ex3_output = None
    if clean_drop_ex3_show.value:
        clean_drop_ex3_output = mo.vstack([
            mo.md("### Expected output"),
            df_drop.drop(columns=["City", "Email"]),
        ])
    clean_drop_ex3_output


@app.cell
def _(mo):
    mo.md(
        """
### Exercise 4

Drop the first and last row, and store the result in `df_trimmed`.
"""
    )


@app.cell
def _(mo):
    clean_drop_ex4_show = mo.ui.checkbox(
        label="Show expected output for Dropping Data, Exercise 4",
        value=False,
    )
    clean_drop_ex4_show
    return clean_drop_ex4_show


@app.cell
def _(df_drop, mo, clean_drop_ex4_show):
    clean_drop_ex4_output = None
    if clean_drop_ex4_show.value:
        clean_drop_ex4_output = mo.vstack([
            mo.md("### Expected output"),
            df_drop.iloc[1:-1],
        ])
    clean_drop_ex4_output


@app.cell
def _(mo):
    mo.md(
        """
## Exercise Set 2: Missing Data

Use this starter code in your own environment:

```python
import pandas as pd
import numpy as np

data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Age": [25, np.nan, 35, 40, None],
    "City": ["NYC", "LA", None, "Miami", "Boston"],
}

df = pd.DataFrame(data)
```
"""
    )


@app.cell
def _(mo):
    mo.md(
        """
### Exercise 1

View the first 5 rows of the DataFrame.
"""
    )


@app.cell
def _(mo):
    clean_missing_ex1_show = mo.ui.checkbox(
        label="Show expected output for Missing Data, Exercise 1",
        value=False,
    )
    clean_missing_ex1_show
    return clean_missing_ex1_show


@app.cell
def _(df_missing, mo, clean_missing_ex1_show):
    clean_missing_ex1_output = None
    if clean_missing_ex1_show.value:
        clean_missing_ex1_output = mo.vstack([
            mo.md("### Expected output"),
            df_missing.head(),
        ])
    clean_missing_ex1_output


@app.cell
def _(mo):
    mo.md(
        """
### Exercise 2

Show where values are missing.
"""
    )


@app.cell
def _(mo):
    clean_missing_ex2_show = mo.ui.checkbox(
        label="Show expected output for Missing Data, Exercise 2",
        value=False,
    )
    clean_missing_ex2_show
    return clean_missing_ex2_show


@app.cell
def _(df_missing, mo, clean_missing_ex2_show):
    clean_missing_ex2_output = None
    if clean_missing_ex2_show.value:
        clean_missing_ex2_output = mo.vstack([
            mo.md("### Expected output"),
            df_missing.isna(),
        ])
    clean_missing_ex2_output


@app.cell
def _(mo):
    mo.md(
        """
### Exercise 3

Count missing values by column.
"""
    )


@app.cell
def _(mo):
    clean_missing_ex3_show = mo.ui.checkbox(
        label="Show expected output for Missing Data, Exercise 3",
        value=False,
    )
    clean_missing_ex3_show
    return clean_missing_ex3_show


@app.cell
def _(df_missing, mo, clean_missing_ex3_show):
    clean_missing_ex3_output = None
    if clean_missing_ex3_show.value:
        clean_missing_ex3_output = mo.vstack([
            mo.md("### Expected output"),
            df_missing.isna().sum(),
        ])
    clean_missing_ex3_output


@app.cell
def _(mo):
    mo.md(
        """
### Exercise 4

Drop rows with missing data.
"""
    )


@app.cell
def _(mo):
    clean_missing_ex4_show = mo.ui.checkbox(
        label="Show expected output for Missing Data, Exercise 4",
        value=False,
    )
    clean_missing_ex4_show
    return clean_missing_ex4_show


@app.cell
def _(df_missing, mo, clean_missing_ex4_show):
    clean_missing_ex4_output = None
    if clean_missing_ex4_show.value:
        clean_missing_ex4_output = mo.vstack([
            mo.md("### Expected output"),
            df_missing.dropna(),
        ])
    clean_missing_ex4_output


@app.cell
def _(mo):
    mo.md(
        """
### Exercise 6

Drop columns with missing data.
"""
    )


@app.cell
def _(mo):
    clean_missing_ex6_show = mo.ui.checkbox(
        label="Show expected output for Missing Data, Exercise 6",
        value=False,
    )
    clean_missing_ex6_show
    return clean_missing_ex6_show


@app.cell
def _(df_missing, mo, clean_missing_ex6_show):
    clean_missing_ex6_output = None
    if clean_missing_ex6_show.value:
        clean_missing_ex6_output = mo.vstack([
            mo.md("### Expected output"),
            df_missing.dropna(axis=1),
        ])
    clean_missing_ex6_output


@app.cell
def _(mo):
    mo.md(
        """
### Exercise 8

Fill missing `Age` values with the mean.
"""
    )


@app.cell
def _(mo):
    clean_missing_ex8_show = mo.ui.checkbox(
        label="Show expected output for Missing Data, Exercise 8",
        value=False,
    )
    clean_missing_ex8_show
    return clean_missing_ex8_show


@app.cell
def _(df_missing, mo, clean_missing_ex8_show):
    clean_missing_ex8_output = None
    if clean_missing_ex8_show.value:
        temp_df_missing_8 = df_missing.copy()
        temp_df_missing_8["Age"] = temp_df_missing_8["Age"].fillna(temp_df_missing_8["Age"].mean())
        clean_missing_ex8_output = mo.vstack([
            mo.md("### Expected output"),
            temp_df_missing_8,
        ])
    clean_missing_ex8_output


@app.cell
def _(mo):
    mo.md(
        """
### Exercise 9

Fill missing `City` values with `"Unknown"`.
"""
    )


@app.cell
def _(mo):
    clean_missing_ex9_show = mo.ui.checkbox(
        label="Show expected output for Missing Data, Exercise 9",
        value=False,
    )
    clean_missing_ex9_show
    return clean_missing_ex9_show


@app.cell
def _(df_missing, mo, clean_missing_ex9_show):
    clean_missing_ex9_output = None
    if clean_missing_ex9_show.value:
        temp_df_missing_9 = df_missing.copy()
        temp_df_missing_9["City"] = temp_df_missing_9["City"].fillna("Unknown")
        clean_missing_ex9_output = mo.vstack([
            mo.md("### Expected output"),
            temp_df_missing_9,
        ])
    clean_missing_ex9_output


@app.cell
def _(mo):
    mo.md(
        """
## Exercise Set 3: Duplicates

Use this starter code in your own environment:

```python
import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie", "Alice", "Bob", "Diana"],
    "Age": [25, 30, 35, 25, 30, 40],
    "City": ["NYC", "LA", "SF", "NYC", "LA", "NYC"],
}

df = pd.DataFrame(data)
```
"""
    )


@app.cell
def _(mo):
    mo.md(
        """
### Exercise 1

Find which rows are duplicates across all columns.
"""
    )


@app.cell
def _(mo):
    clean_dup_ex1_show = mo.ui.checkbox(
        label="Show expected output for Duplicates, Exercise 1",
        value=False,
    )
    clean_dup_ex1_show
    return clean_dup_ex1_show


@app.cell
def _(df_duplicates, mo, clean_dup_ex1_show):
    clean_dup_ex1_output = None
    if clean_dup_ex1_show.value:
        clean_dup_ex1_output = mo.vstack([
            mo.md("### Expected output"),
            df_duplicates.duplicated(),
        ])
    clean_dup_ex1_output


@app.cell
def _(mo):
    mo.md(
        """
### Exercise 2

Drop duplicate rows, keeping the first occurrence.
"""
    )


@app.cell
def _(mo):
    clean_dup_ex2_show = mo.ui.checkbox(
        label="Show expected output for Duplicates, Exercise 2",
        value=False,
    )
    clean_dup_ex2_show
    return clean_dup_ex2_show


@app.cell
def _(df_duplicates, mo, clean_dup_ex2_show):
    clean_dup_ex2_output = None
    if clean_dup_ex2_show.value:
        clean_dup_ex2_output = mo.vstack([
            mo.md("### Expected output"),
            df_duplicates.drop_duplicates(keep="first"),
        ])
    clean_dup_ex2_output


@app.cell
def _(mo):
    mo.md(
        """
### Exercise 3

Drop duplicate rows, keeping only the last occurrence.
"""
    )


@app.cell
def _(mo):
    clean_dup_ex3_show = mo.ui.checkbox(
        label="Show expected output for Duplicates, Exercise 3",
        value=False,
    )
    clean_dup_ex3_show
    return clean_dup_ex3_show


@app.cell
def _(df_duplicates, mo, clean_dup_ex3_show):
    clean_dup_ex3_output = None
    if clean_dup_ex3_show.value:
        clean_dup_ex3_output = mo.vstack([
            mo.md("### Expected output"),
            df_duplicates.drop_duplicates(keep="last"),
        ])
    clean_dup_ex3_output


@app.cell
def _(mo):
    mo.md(
        """
### Exercise 4

Drop all duplicates, removing both the original and duplicate rows.
"""
    )


@app.cell
def _(mo):
    clean_dup_ex4_show = mo.ui.checkbox(
        label="Show expected output for Duplicates, Exercise 4",
        value=False,
    )
    clean_dup_ex4_show
    return clean_dup_ex4_show


@app.cell
def _(df_duplicates, mo, clean_dup_ex4_show):
    clean_dup_ex4_output = None
    if clean_dup_ex4_show.value:
        clean_dup_ex4_output = mo.vstack([
            mo.md("### Expected output"),
            df_duplicates.drop_duplicates(keep=False),
        ])
    clean_dup_ex4_output


@app.cell
def _(mo):
    mo.md(
        """
---
# Section 3: Data Wrangling Essentials
"""
    )


@app.cell
def _(mo):
    mo.md(
        """
## Exercise Set 1: Renaming Columns

Use this starter code in your own environment:

```python
import pandas as pd

data = {
    "fname": ["Alice", "Bob", "Charlie"],
    "lname": ["Smith", "Jones", "Brown"],
    "ctry": ["USA", "Canada", "UK"],
}

df = pd.DataFrame(data)
```
"""
    )


@app.cell
def _(mo):
    mo.md(
        """
### Exercise 1

Change `fname` to `FirstName` and `lname` to `LastName`.
"""
    )


@app.cell
def _(mo):
    wrangle_rename_ex1_show = mo.ui.checkbox(
        label="Show expected output for Renaming Columns, Exercise 1",
        value=False,
    )
    wrangle_rename_ex1_show
    return wrangle_rename_ex1_show


@app.cell
def _(df_rename, mo, wrangle_rename_ex1_show):
    wrangle_rename_ex1_output = None
    if wrangle_rename_ex1_show.value:
        wrangle_rename_ex1_output = mo.vstack([
            mo.md("### Expected output"),
            df_rename.rename(columns={"fname": "FirstName", "lname": "LastName"}),
        ])
    wrangle_rename_ex1_output


@app.cell
def _(mo):
    mo.md(
        """
### Exercise 2

Change all column names to: `['FirstName', 'LastName', 'Country']`
"""
    )


@app.cell
def _(mo):
    wrangle_rename_ex2_show = mo.ui.checkbox(
        label="Show expected output for Renaming Columns, Exercise 2",
        value=False,
    )
    wrangle_rename_ex2_show
    return wrangle_rename_ex2_show


@app.cell
def _(df_rename, mo):
    renamed_all_df = df_rename.copy()
    renamed_all_df.columns = ["FirstName", "LastName", "Country"]
    return renamed_all_df


@app.cell
def _(mo, renamed_all_df, wrangle_rename_ex2_show):
    wrangle_rename_ex2_output = None
    if wrangle_rename_ex2_show.value:
        wrangle_rename_ex2_output = mo.vstack([
            mo.md("### Expected output"),
            renamed_all_df,
        ])
    wrangle_rename_ex2_output


@app.cell
def _(mo):
    mo.md(
        """
## Exercise Set 2: Reordering Columns

Use this starter code in your own environment:

```python
import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Dept": ["HR", "Finance", "IT"],
    "Sal": [60000, 70000, 80000],
}

df = pd.DataFrame(data)
```
"""
    )


@app.cell
def _(mo):
    mo.md(
        """
### Exercise 1

Rename `Dept` to `Department` and `Sal` to `Salary`.
"""
    )


@app.cell
def _(mo):
    wrangle_reorder_ex1_show = mo.ui.checkbox(
        label="Show expected output for Reordering Columns, Exercise 1",
        value=False,
    )
    wrangle_reorder_ex1_show
    return wrangle_reorder_ex1_show


@app.cell
def _(df_reorder, mo):
    reordered_renamed_df = df_reorder.rename(columns={"Dept": "Department", "Sal": "Salary"})
    return reordered_renamed_df


@app.cell
def _(mo, reordered_renamed_df, wrangle_reorder_ex1_show):
    wrangle_reorder_ex1_output = None
    if wrangle_reorder_ex1_show.value:
        wrangle_reorder_ex1_output = mo.vstack([
            mo.md("### Expected output"),
            reordered_renamed_df,
        ])
    wrangle_reorder_ex1_output


@app.cell
def _(mo):
    mo.md(
        """
### Exercise 2

Reorder columns so `Salary` appears first, followed by `Name` and `Department`.
"""
    )


@app.cell
def _(mo):
    wrangle_reorder_ex2_show = mo.ui.checkbox(
        label="Show expected output for Reordering Columns, Exercise 2",
        value=False,
    )
    wrangle_reorder_ex2_show
    return wrangle_reorder_ex2_show


@app.cell
def _(mo, reordered_renamed_df, wrangle_reorder_ex2_show):
    wrangle_reorder_ex2_output = None
    if wrangle_reorder_ex2_show.value:
        wrangle_reorder_ex2_output = mo.vstack([
            mo.md("### Expected output"),
            reordered_renamed_df[["Salary", "Name", "Department"]],
        ])
    wrangle_reorder_ex2_output


@app.cell
def _(mo):
    mo.md(
        """
### Exercise 3

Print the updated DataFrame.
"""
    )


@app.cell
def _(mo):
    wrangle_reorder_ex3_show = mo.ui.checkbox(
        label="Show expected output for Reordering Columns, Exercise 3",
        value=False,
    )
    wrangle_reorder_ex3_show
    return wrangle_reorder_ex3_show


@app.cell
def _(mo, reordered_renamed_df, wrangle_reorder_ex3_show):
    wrangle_reorder_ex3_output = None
    if wrangle_reorder_ex3_show.value:
        wrangle_reorder_ex3_output = mo.vstack([
            mo.md("### Expected output"),
            reordered_renamed_df[["Salary", "Name", "Department"]],
        ])
    wrangle_reorder_ex3_output


@app.cell
def _(mo):
    mo.md(
        """
## Exercise Set 3: GroupBy and Agg

Use this starter code in your own environment:

```python
import pandas as pd

data = {
    "Store": ["A", "A", "A", "B", "B", "C", "C", "C", "C"],
    "Product": ["Apples", "Oranges", "Bananas", "Apples", "Bananas", "Oranges", "Apples", "Bananas", "Bananas"],
    "Sales": [100, 80, 90, 120, 110, 60, 95, 85, 75],
    "Profit": [30, 25, 20, 40, 35, 15, 32, 22, 18],
}

df = pd.DataFrame(data)
print(df.head())
```
"""
    )


@app.cell
def _(mo):
    mo.md(
        """
### Exercise 1

Group the data by `Store` and use `.agg()` to find the average `Sales` and average `Profit` for each store.
"""
    )


@app.cell
def _(mo):
    wrangle_group_ex1_show = mo.ui.checkbox(
        label="Show expected output for GroupBy and Agg, Exercise 1",
        value=False,
    )
    wrangle_group_ex1_show
    return wrangle_group_ex1_show


@app.cell
def _(df_group, mo, wrangle_group_ex1_show):
    wrangle_group_ex1_output = None
    if wrangle_group_ex1_show.value:
        wrangle_group_ex1_output = mo.vstack([
            mo.md("### Expected output"),
            df_group.groupby("Store").agg({"Sales": "mean", "Profit": "mean"}),
        ])
    wrangle_group_ex1_output


@app.cell
def _(mo):
    mo.md(
        """
### Exercise 2

Group by `Product` and get the maximum `Sales` and minimum `Profit`.
"""
    )


@app.cell
def _(mo):
    wrangle_group_ex2_show = mo.ui.checkbox(
        label="Show expected output for GroupBy and Agg, Exercise 2",
        value=False,
    )
    wrangle_group_ex2_show
    return wrangle_group_ex2_show


@app.cell
def _(df_group, mo, wrangle_group_ex2_show):
    wrangle_group_ex2_output = None
    if wrangle_group_ex2_show.value:
        wrangle_group_ex2_output = mo.vstack([
            mo.md("### Expected output"),
            df_group.groupby("Product").agg({"Sales": "max", "Profit": "min"}),
        ])
    wrangle_group_ex2_output


@app.cell
def _(mo):
    mo.md(
        """
### Exercise 3

Group by `Store` and return the average `Sales` and maximum `Profit`, but name the columns `Avg_Sales` and `Max_Profit`.
"""
    )


@app.cell
def _(mo):
    wrangle_group_ex3_show = mo.ui.checkbox(
        label="Show expected output for GroupBy and Agg, Exercise 3",
        value=False,
    )
    wrangle_group_ex3_show
    return wrangle_group_ex3_show


@app.cell
def _(df_group, mo, wrangle_group_ex3_show):
    wrangle_group_ex3_output = None
    if wrangle_group_ex3_show.value:
        wrangle_group_ex3_output = mo.vstack([
            mo.md("### Expected output"),
            df_group.groupby("Store").agg(
                Avg_Sales=("Sales", "mean"),
                Max_Profit=("Profit", "max"),
            ),
        ])
    wrangle_group_ex3_output


@app.cell
def _(mo):
    mo.md(
        """
### Exercise 4

BONUS: Group by both `Store` and `Product`, and find the total `Sales` using `.agg()`.
"""
    )


@app.cell
def _(mo):
    wrangle_group_ex4_show = mo.ui.checkbox(
        label="Show expected output for GroupBy and Agg, Exercise 4",
        value=False,
    )
    wrangle_group_ex4_show
    return wrangle_group_ex4_show


@app.cell
def _(df_group, mo, wrangle_group_ex4_show):
    wrangle_group_ex4_output = None
    if wrangle_group_ex4_show.value:
        wrangle_group_ex4_output = mo.vstack([
            mo.md("### Expected output"),
            df_group.groupby(["Store", "Product"]).agg({"Sales": "sum"}),
        ])
    wrangle_group_ex4_output


@app.cell
def _(mo):
    mo.md(
        """
## Exercise Set 4: Joining

Use this starter code in your own environment:

```python
import pandas as pd

df_customers = pd.DataFrame({
    "CustomerName": ["Alice", "Bob", "Charlie"]
}, index=[101, 102, 103])

df_orders = pd.DataFrame({
    "OrderTotal": [250, 300, 400]
}, index=[101, 102, 103])
```
"""
    )


@app.cell
def _(mo):
    mo.md(
        """
### Exercise 1

Join `df_orders` to `df_customers` on the index.
"""
    )


@app.cell
def _(mo):
    wrangle_join_ex1_show = mo.ui.checkbox(
        label="Show expected output for Joining, Exercise 1",
        value=False,
    )
    wrangle_join_ex1_show
    return wrangle_join_ex1_show


@app.cell
def _(df_customers, df_orders, mo, wrangle_join_ex1_show):
    wrangle_join_ex1_output = None
    if wrangle_join_ex1_show.value:
        wrangle_join_ex1_output = mo.vstack([
            mo.md("### Expected output"),
            df_customers.join(df_orders),
        ])
    wrangle_join_ex1_output


@app.cell
def _(mo):
    mo.md(
        """
### Exercise 2

Add a new column to `df_customers` with city data from `df_cities`.
"""
    )


@app.cell
def _(mo):
    wrangle_join_ex2_show = mo.ui.checkbox(
        label="Show expected output for Joining, Exercise 2",
        value=False,
    )
    wrangle_join_ex2_show
    return wrangle_join_ex2_show


@app.cell
def _(df_cities, df_customers, mo, wrangle_join_ex2_show):
    wrangle_join_ex2_output = None
    if wrangle_join_ex2_show.value:
        wrangle_join_ex2_output = mo.vstack([
            mo.md("### Expected output"),
            df_customers.join(df_cities),
        ])
    wrangle_join_ex2_output


if __name__ == "__main__":
    app.run()
