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


'''
Prints:

Original dataframe:
    Name   Position  Salary
0  Name1  Scientist     101
1  Name2  Scientist      93
2  Name3     Lawyer     150
3  Name4   Engineer      90
4  Name5    Teacher      90
5  Name6      Other       0

Dataframe with scientists only:
0    Name1
1    Name2
Name: Name, dtype: object

Dataframe with added weekly wage:
    Name   Position  Salary  Weekly wage
0  Name1  Scientist     101      1803.57
1  Name2  Scientist      93      1660.71
2  Name3     Lawyer     150      2678.57
3  Name4   Engineer      90      1607.14
4  Name5    Teacher      90      1607.14
5  Name6      Other       0         0.00

Dataframe with Name6's row removed:
    Name   Position  Salary  Weekly wage
0  Name1  Scientist     101      1803.57
1  Name2  Scientist      93      1660.71
2  Name3     Lawyer     150      2678.57
3  Name4   Engineer      90      1607.14
4  Name5    Teacher      90      1607.14
'''
