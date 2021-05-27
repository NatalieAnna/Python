# Uses Salary.xlsx

import pandas as pd
import numpy as np  # cleans up NaN values using .dropna()

# creates new dataframe and copies Salary.xlxs's data into it
df = pd.read_excel("Salary.xlsx")
print("Original dataframe:")
print(df)

# Prints column Name where Position is equal to Scientist
salary = df['Name'].where(df['Position'] == 'Scientist').dropna()
print()
print("Dataframe with scientists only:")
print(salary)

# Calculates weekly wage from column Salary and adds values to new column
for ind, row in df.iterrows():
    df.loc[ind, 'Weekly wage'] = row['Salary'] * 1000 / 56
    df = df.round(2)    # rounds weekly wage to 2 decimal places
print()
print("Dataframe with added weekly wage:")
print(df)

# Deletes row from dataframe with an element (need to find element's index first)
get_index = df[df['Name']=='Name6'].index
df.drop(get_index, inplace=True)
print()
print("Dataframe with Name6's row removed:")
print(df)
