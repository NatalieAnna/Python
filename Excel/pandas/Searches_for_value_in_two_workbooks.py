# searches excel for value (ie Breed (col) of dog (row) with Activity (col) == "Low")

import pandas as pd
import numpy as np  # cleans up NaN values using .dropna()

excel_files = ["Dogs.xlsx", "Dogs2.xlsx"]

for file in excel_files:
    df = pd.read_excel(file)
    low = df["Breed"].where(df["Activity"] == "Low").dropna()    # both excel files must have column "Activity"
    print(file)
    print(low)



"""
Prints:

Dogs.xlsx
1    Spoodle
Name: Breed, dtype: object
Dogs2.xlsx
Series([], Name: Breed, dtype: object)

"""
