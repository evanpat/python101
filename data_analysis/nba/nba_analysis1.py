import pandas as pd

df = pd.read_csv('final_data.csv')

print(df.head(10))

# SQL: select first, last, team from nba_data
selected_columns = ['first', 'last', 'team']
df_selected = df[selected_columns]
print(df_selected.head(10))

# SQL: select first, last, team from nba_data where year >= 2000
df_selected1 = df.loc[(df['year'] >= 2000) & (df['year'] <= 2015), selected_columns]
print(df_selected1.head(10))

# SQL: select first, last, sum(games_played) from nba_data group by first, last
df_selected2 = df.groupby(['first', 'last'])['games_played'].sum().sort_values(ascending=False)
print(df_selected2.head(10))

# SQL: select first, last, sum(games_played), average(pts) from nba_data group by first, last
df_selected3 = df.groupby(['first', 'last']).agg({
    'games_played': 'sum',
    'pts': 'mean'
}).rename(columns={
    'games_played': 'Total Games',
    'pts': 'Average Points'
}).sort_values(by=['Average Points'], ascending=False)
print(df_selected3.head(20))