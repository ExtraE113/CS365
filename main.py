import pandas as pd

# Load the CSV from the provided URL
url = "https://raw.githubusercontent.com/evelinag/StarWars-social-network/master/data/characters.csv"
characters_df = pd.read_csv(url, header=None)

# Pre-process the names to split into first and last names and generate emails
# Skip entries with no spaces (single-word names)
processed_characters = []
for name in characters_df[0]:
    parts = name.split()
    if len(parts) > 1:
        first_name = parts[0]
        last_name = ' '.join(parts[1:])
        email = f"{first_name.lower()}.{last_name.replace(' ', '').lower()}@example.com"
        processed_characters.append([first_name, last_name, email])

# Convert the list to a DataFrame
processed_characters_df = pd.DataFrame(processed_characters, columns=["first_name", "last_name", "email"])

# Save to a CSV file
csv_path = "./processed_star_wars_characters.csv"
processed_characters_df.to_csv(csv_path, index=False)
print(f"Processed characters saved to {csv_path}")