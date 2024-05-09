import numpy as np
import pandas as pd

# Create DataFrame
data = {
    "districts": ["d1", "d2", "d3", "d4"],
    "mandates": [5, 10, 15, 30],
    "votes_A": [200, 400, 200, 90],
    "votes_B": [300, 200, 900, 50],
    "votes_C": [500, 100, 50, 1000]
}
frame = pd.DataFrame(data)

# Function to apply the Hondt method
def apply_hondt(votes, mandates):
    distribution = np.zeros_like(votes)
    for i in range(mandates):
        quotient = votes / (distribution + 1)
        party_index = np.argmax(quotient)
        distribution[party_index] += 1
    return distribution

# Apply Hondt method to each district
for i, row in frame.iterrows():
    votes = row[['votes_A', 'votes_B', 'votes_C']].values
    mandates = row['mandates']
    frame.loc[i, ['mandates_A', 'mandates_B', 'mandates_C']] = apply_hondt(votes, mandates)

print(frame)

for i, row in frame.iterrows():
    votes = row[['votes_A', 'votes_B', 'votes_C']].values
    print(votes)
    mandates = row['mandates']
    print(mandates)