import pandas as pd

data = pd.read_excel("dataProject4.xlsx",sheet_name="20000-211000")
df = pd.DataFrame(data)

# duplicates rows
if df.duplicated().any():
    print("Warning: The data contains duplicate rows.")
    df.drop_duplicates()
    print("Duplicates removed.")
else:
    print("No duplicates found")

# missing values
if df.isnull().values.any():
    print("Warning: The data contains missing values.")
else:
    print("No missing values found")


value_to_remove = 'Result'
df = df[df['Column1'] != value_to_remove]
df = df.reset_index(drop=True)

# validate data of column name of customer number
df.iloc[3,0] = 'Customer number'
df.iloc[3,5] = 'Brand name'
df.iloc[1,6] = 'Business subfilter'
df.iloc[0,6] = 'Business Filter'

# handling missing data: delete result row
rows_to_delete = [73,103,167,170]
df = df.drop(rows_to_delete)
df = df.reset_index(drop=True)

# 