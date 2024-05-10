import numpy as np
from typing import List

# Importing from relative path
from src.input_data1 import parties, votes_per_party, seats_per_district, num_districts

def distribute_compensation_seats(percentages: np.ndarray, seats: int) -> np.ndarray:
    """
    Distribute compensation seats among parties based on their vote percentages.

    Args:
        percentages (np.ndarray): Array of vote percentages for each party.
        seats (int): Total number of seats to be distributed.

    Returns:
        np.ndarray: Array of seats distributed to each party.
    """
    seats_per_party = np.round(percentages * seats)  # Distribute seats based on percentage of votes
    remaining_seats = seats - np.sum(seats_per_party)  # Calculate remaining seats

    if remaining_seats > 0:
        # Distribute remaining seats to parties with the highest decimal fractions
        decimal_fractions = percentages - seats_per_party / seats
        order = np.argsort(-decimal_fractions)
        seats_per_party[order[:remaining_seats]] += 1

    return seats_per_party

def main():
    # Defining input data
    total_votes = np.sum(votes_per_party)  # Total votes
    percentage_votes_per_party = votes_per_party / total_votes  # Percentage of votes per party
    compensation_seats = 20  # Total number of compensation seats to be distributed

    # Distributing compensation seats
    compensation_seats_per_party = distribute_compensation_seats(percentage_votes_per_party, compensation_seats)

    # Results
    print("Compensation Seats per Party:")
    print(compensation_seats_per_party)

if __name__ == "__main__":
    main()