import numpy as np

from src.input_data1 import parties, votes_per_party, seats_per_district, num_districts

# Function to apply the Hondt method
def apply_hondt(votes, seats):
    distribution = np.zeros(len(votes))
    for _ in range(seats):
        votes = votes / (distribution + 1)
        party_winner = np.argmax(votes)
        distribution[party_winner] += 1
    return distribution

# Simulating seat distribution in each electoral district
seats_per_party = np.zeros((len(parties), num_districts))
for i in range(num_districts):
    seats_per_party[:, i] = apply_hondt(votes_per_party, seats_per_district)

# Results
print("Seat Distribution per Electoral District:")
print(seats_per_party)
