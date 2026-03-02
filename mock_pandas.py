import numpy as np
import pandas as pd

def mock_data(n=10000):
    incomes = np.random.choice(["Low Income", "Medium Income", "High Income"], n, p=[0.5, 0.3, 0.2])
    scores = np.random.uniform(200, 1000, n)
    return pd.DataFrame({"income": incomes, "score": scores})

def transform_data(df):
    bins = [0, 599, 699, 799, 899, 1000]
    labels = ["200-599", "600-699", "700-799", "800-899", "900-1000"]
    df['score_range'] = pd.cut(df['score'], bins=bins, labels=labels)

    table = pd.crosstab(df['score_range'], df['income'])
    table['total_scores'] = table.sum(axis=1)

    for income_column in ["Low Income", "Medium Income", "High Income"]:
        percentage_col_name = f"percentage_{income_column.lower().replace(' ', '_')}"
        table[percentage_col_name] = round((table[income_column] / table['total_scores']) * 100, 1)

    table = table.replace({float('nan'): None})

    return table.to_dict(orient="index")

students = mock_data(20)
datasets = transform_data(students)

for key, dataset in datasets.items():
    print(key)
    print(dataset)
    print("\n")