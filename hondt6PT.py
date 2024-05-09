import numpy as np
import pandas as pd

# import csv file
df = pd.read_csv('data/votos_AR_2024.csv')

# print the first 5 rows of the DataFrame
print(df.head())

# select all columns from df except 'código'    
df2 = df.loc[:, df.columns != 'código']

# print the first 5 rows of the DataFrame
print(df2.head())

df2.columns = df2.columns.str.replace('.', '')

# Function to apply the Hondt method
def apply_hondt(votes, mandates):
    distribution = np.zeros_like(votes)
    for i in range(mandates):
        quotient = votes / (distribution + 1)
        party_index = np.argmax(quotient)
        distribution[party_index] += 1
    return distribution

# create an array where each element is the concatenation of the string "mandatos" with the name of the party   
mandates_columns = ['mandatos_' + party for party in ['ADN', 'BE', 'CH', 'E', 'IL', 'JPP',
       'L', 'MPTA', 'NC', 'ND', 'PAN', 'PCP-PEV', 'PCTP/MRPP', 'PPD/PSDCDS-PP',
       'PPD/PSDCDS-PPPPM', 'PPM', 'PS', 'PTP', 'RIR', 'VP']]
print(mandates_columns)

# Apply Hondt method to each district
for i, row in df2.iterrows():
    votes = row[['ADN', 'BE', 'CH', 'E', 'IL', 'JPP',
       'L', 'MPTA', 'NC', 'ND', 'PAN', 'PCP-PEV', 'PCTP/MRPP', 'PPD/PSDCDS-PP',
       'PPD/PSDCDS-PPPPM', 'PPM', 'PS', 'PTP', 'RIR', 'VP']].values
    mandates = row['mandatos']
    df2.loc[i, mandates_columns] = apply_hondt(votes, mandates)

print(df2)
# save df2 as a csv file    
df2.to_csv('data/mandatos_AR_2024.csv', index=False, sep=';', decimal=',')

