import numpy as np
import pandas as pd

def load_and_clean_data(file_path):
    # Load data
    df = pd.read_csv(file_path)
    
    # Remove 'código' column
    df_cleaned = df.drop(columns=['código'])
    
    # Remove dots from column names
    df_cleaned.columns = df_cleaned.columns.str.replace('.', '')
    
    return df_cleaned

def apply_hondt(votes, mandates):
    distribution = np.zeros_like(votes)
    for i in range(mandates):
        quotient = votes / (distribution + 1)
        party_index = np.argmax(quotient)
        distribution[party_index] += 1
    return distribution

def distribute_compensation_seats(percentages, seats):
    seats_per_party = np.round(percentages * seats)
    remaining_seats = int(seats - np.sum(seats_per_party))
    if remaining_seats > 0:
        decimal_fractions = percentages - seats_per_party / seats
        order = np.argsort(-decimal_fractions)
        seats_per_party[order[:remaining_seats]] += 1
    return seats_per_party

def main():
    # Load and clean data
    file_path = 'data/votos_AR_2024.csv'
    df = load_and_clean_data(file_path)
    
    # Calculate percentage of votes per party
    total_votes = df.drop(columns=['nome do território', 'mandatos']).sum()
    percentage_votes_per_party = total_votes / total_votes.sum()
    percentage_votes_per_party = percentage_votes_per_party.to_numpy()  # Convert to numpy array
    
    # Total mandates and compensation seats
    total_mandates = df['mandatos'].sum()
    compensation_percentage = 0.1
    compensation_seats = int(np.floor(compensation_percentage * total_mandates))
    
    # Distribute compensation seats
    compensation_seats_per_party = distribute_compensation_seats(percentage_votes_per_party, compensation_seats)
    
    # Create DataFrame with compensation seats per party
    compensation_seats_df = pd.DataFrame(compensation_seats_per_party, index=total_votes.index, columns=['mandatos'])
    compensation_seats_df = compensation_seats_df.astype(int)  # Convert to integers
    
    # Print results
    print("Compensation Seats per Party:")
    print(compensation_seats_df)
    
    # Save results to CSV
    # compensation_seats_df.to_csv('data/mandatos_compensatorios_AR_2024.csv', sep=';', decimal=',')

if __name__ == "__main__":
    main()