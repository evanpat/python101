# https://www.kaggle.com/datasets/ethankeyes/nba-all-star-players-and-stats-1980-2022/data
# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Read CSV file into a DataFrame
# Replace the file path with the actual path to your CSV file
df = pd.read_csv("final_data.csv")

# Print the first 10 rows of the DataFrame
print(df.head(10))

from itertools import groupby

# Grouping data by unique pairs of 'first' and 'last' names and counting the occurrences
seasons = np.array([(key[0], key[1], len(list(group))) for key, group in groupby(sorted(zip(df["first"], df["last"])))]) 

# Function to convert a specified column to float by position
def col_to_float_by_position(df, column_position):
    # Check if the specified column position is valid
    if 0 <= column_position < len(df.columns):
        col_name = df.columns[column_position]
        # Convert the specified column to float
        df[col_name] = df[col_name].astype(float)
    else:
        # Print an error message for an invalid column position
        print(f"Invalid column position: {column_position}")
    
    return df

# Convert the third column ('Seasons_played') to float using the defined function
seasons = col_to_float_by_position(pd.DataFrame(seasons, columns=['First', 'Last', 'Seasons_played']), 2)

# Filter for players with 10 or more seasons played
seasons = seasons[seasons['Seasons_played'] >= 10]

# Sort the DataFrame by the number of seasons played in descending order
seasons = seasons.sort_values(by='Seasons_played', ascending=False)

# Print the top 10 players with the most seasons played
print("Top 10 players with the most seasons played\n", seasons.head(10))



# Sort the DataFrame by 'first' and 'last' columns
sorted_df = df.sort_values(by=['first', 'last'])

# Group the data by unique pairs of 'first' and 'last' and calculate the sum of 'games_played'
games = np.array([(key[0], key[1], sum(group['games_played'])) for key, group in sorted_df.groupby(['first', 'last'])])

# Convert the third column ('Games_played') to float using the defined function
games = col_to_float_by_position(pd.DataFrame(games, columns=['First', 'Last', 'Games_played']), 2)

# Sort the DataFrame by the number of games played in descending order
games = games.sort_values(by='Games_played', ascending=False)

# Print the top 10 players with the most games played
print("Top 10 players with the most Games Played\n", games.head(10))

# Remove rows with missing values in the 'pts' or 'fta' columns
df.dropna(subset=['pts', 'fta'], inplace=True)

# Perform linear regression to analyze the correlation between average points per game and average free throws attempted
a, b = np.polyfit(df['pts'], df['fta'], 1)

# Scatter plot of points per game against free throws attempted
plt.scatter(df['pts'], df['fta'], label='Free Throw Attempts', color='purple')
plt.xlabel('Points per Game')
plt.ylabel('Free Throws Attempted')

# Plot the regression line
plt.plot(df['pts'], a * df['pts'] + b, label='Regression Line', color='blue')

# Display the legend
plt.legend()

# Display the plot
plt.show()