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
# df2.to_csv('data/mandatos_AR_2024.csv', index=False, sep=';', decimal=',')

# compute the total number of votes for each party  
total_votes = df2[['ADN', 'BE', 'CH', 'E', 'IL', 'JPP',
       'L', 'MPTA', 'NC', 'ND', 'PAN', 'PCP-PEV', 'PCTP/MRPP', 'PPD/PSDCDS-PP',
       'PPD/PSDCDS-PPPPM', 'PPM', 'PS', 'PTP', 'RIR', 'VP']].sum()

# compute percentage of votes for each party    
percentage_votes_per_party = total_votes / total_votes.sum()
# Convert series to numpy array.
percentage_votes_per_party = percentage_votes_per_party.to_numpy() 

# total mandates to be distributed in Continental Portugal
total_mandates = df2['mandatos'].sum()
compensation_percentage = 0.1
compensation_seats = int(np.floor(compensation_percentage * total_mandates))
print(compensation_seats)

# Function to distribute compensation seats
def distribute_compensation_seats(percentages, seats):
    seats_per_party = np.round(percentages * seats)  # Distribute seats based on percentage of votes
    remaining_seats = int(seats - np.sum(seats_per_party))  # Calculate remaining seats
    if remaining_seats > 0:
        # Distribute remaining seats to parties with the highest decimal fractions
        decimal_fractions = percentages - seats_per_party / seats
        order = np.argsort(-decimal_fractions)
        seats_per_party[order[:remaining_seats]] += 1
    return seats_per_party

# Distributing compensation seats
compensation_seats_per_party = distribute_compensation_seats(percentage_votes_per_party, compensation_seats)

# show the compensation seats per party in a dataframe with the party names as index    
compensation_seats_per_party = pd.DataFrame(compensation_seats_per_party, index=total_votes.index)
# transform compensation_seats_per_party into an integer    
compensation_seats_per_party = compensation_seats_per_party.astype(int)
compensation_seats_per_party.columns = ['mandatos'] 

# Results
print("Compensation Seats per Party:")
print(compensation_seats_per_party)

# save compensation_seats_per_party as a csv file   
# compensation_seats_per_party.to_csv('data/mandatos_compensatorios_AR_2024.csv', sep=';', decimal=',')
