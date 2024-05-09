import numpy as np

# Defining input data
total_votes = np.sum(votes_per_party)  # Total votes
percentage_votes_per_party = votes_per_party / total_votes  # Percentage of votes per party
compensation_seats = 20  # Total number of compensation seats to be distributed

# Function to distribute compensation seats
def distribute_compensation_seats(percentages, seats):
    seats_per_party = np.round(percentages * seats)  # Distribute seats based on percentage of votes
    remaining_seats = seats - np.sum(seats_per_party)  # Calculate remaining seats
    if remaining_seats > 0:
        # Distribute remaining seats to parties with the highest decimal fractions
        decimal_fractions = percentages - seats_per_party / seats
        order = np.argsort(-decimal_fractions)
        seats_per_party[order[:remaining_seats]] += 1
    return seats_per_party

# Distributing compensation seats
compensation_seats_per_party = distribute_compensation_seats(percentage_votes_per_party, compensation_seats)

# Results
print("Compensation Seats per Party:")
print(compensation_seats_per_party)
