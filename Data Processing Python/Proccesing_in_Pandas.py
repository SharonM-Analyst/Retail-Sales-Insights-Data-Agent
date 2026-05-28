import pandas as pd 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sweetviz as sv


df = spark.table("workspace.default.retail_sales").toPandas()
df.head(10)

# Convert to datetime first (use the actual column name)

df['Date'] = pd.to_datetime(df['Date'])

# Month Name
df['Month_name'] = df['Date'].dt.month_name()

# Quarter
df['Quarter'] = 'Q' + df['Date'].dt.quarter.astype(str)

# Day Name
df['Day_name'] = df['Date'].dt.day_name()

# Weekend / Weekday Category
df['day_category'] = np.where(
    df['Date'].dt.dayofweek >= 5,
    'Weekend',
    'Weekday'
)

# Season Pattern (Southern Hemisphere - South Africa)
def season_pattern(month):
    if month in [12, 1, 2]:
        return 'Summer'
    elif month in [3, 4, 5]:
        return 'Autumn'
    elif month in [6, 7, 8]:
        return 'Winter'
    else:
        return 'Spring'

df['season_pattern'] = df['Date'].dt.month.apply(season_pattern)


# Create Age Groups
df['Age_Group'] = pd.cut(
    df['Age'],
    bins=[17, 24, 34, 44, 54, 64],
    labels=[
        '18-24 Young Adults',
        '25-34 Adults',
        '35-44 Mid Adults',
        '45-54 Mature Adults',
        '55-64 Seniors'
    ]
)

# Create Spending Index
conditions = [
    df['Total Amount'] < 100,
    (df['Total Amount'] >= 100) &
    (df['Total Amount'] < 500),
    df['Total Amount'] >= 500
]

choices = [
    'Low Spender',
    'Medium Spender',
    'High Spender'
]

df['spending_index'] = np.select(
    conditions,
    choices,
    default='Unknown'
)

# Revenue and AOV calculation per customer
summary = (
    df.groupby('CustomerID')
      .agg(
          Revenue=('Total Amount', 'sum'),
          Orders=('TransactionID', 'nunique')
      )
      .reset_index()
)

# Average Order Value
summary['AOV'] = (
    summary['Revenue'] /
    summary['Orders']
)

# Merge AOV back into original table
df = df.merge(
    summary[['CustomerID', 'Revenue', 'AOV']],
    on='CustomerID',
    how='left'
)

print(df.head())
