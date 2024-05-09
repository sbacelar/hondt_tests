import numpy as np

# Define the number of parties, districts, votes, and mandates
num_parties = 3
num_districts = 4
votes = np.array([[200, 300, 500], [400, 200, 100], [200, 900, 50], [90, 50, 1000]])
mandates_per_district = np.array([5, 10, 15, 30])

# Function to apply the Hondt method
def apply_hondt(votes, mandates):
    distribution = np.zeros_like(votes)
    for i in range(mandates):
        quotient = votes / (distribution + 1)
        party_index = np.argmax(quotient)
        distribution[party_index] += 1
    return distribution

# Distribute mandates in each district
mandates_distribution = np.zeros((num_parties, num_districts))
for district in range(num_districts):
    mandates_distribution[:, district] = apply_hondt(votes[district, :], mandates_per_district[district])

# Print the distribution of mandates in each district
for district, mandates in enumerate(mandates_distribution.T, start=1):
    print(f"District {district}: {mandates}")


