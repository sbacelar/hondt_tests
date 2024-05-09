import pandas as pd

# Specify the path to the Excel file
excel_file = 'data/AR_2024_Globais.xlsx'

# Specify the name of the sheet you want to import
sheet_name = 'AR_2024_Distrito_Reg.Autónoma'

# Read the Excel file into a DataFrame
df = pd.read_excel(excel_file, sheet_name=sheet_name)

# Print the DataFrame
print(df)

# delete first 3 rows of df
df2 = df.iloc[4:24]

print(df2)

# row of df with index=2 is the header of df2   
df2.columns = df.iloc[2]
print(df2)

print(df2.columns.tolist())

df3 = df2.iloc[:, [0, 1, 13, 14, 17, 20, 23, 26, 29, 32, 35, 38, 41, 44, 47, 50, 53, 56, 59,
                   62, 65, 68, 71]]
print(df3)