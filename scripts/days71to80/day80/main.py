import pandas as pd
import matplotlib.pyplot as plt

# Data import and column renaming
df = pd.read_csv('QueryResults.csv', names=['DATE', 'TAG', 'POSTS'])

# Initial data investigation
print(df.head())
print(df.shape)
print(df.count())

# Identify the programming language with the most posts
print(df.groupby('TAG').sum())

# Find how many months of entries per language
print(df.groupby('TAG').count())

# Convert the date column into a date-time object
df.DATE = pd.to_datetime(df.DATE)
print(type(df.DATE[1]))

# Pivot the dataframe
pivoted_df = df.pivot(index='DATE', columns='TAG', values='POSTS').fillna(0)

print(pivoted_df.shape)
print(pivoted_df.head())
print(pivoted_df.tail())
print(pivoted_df.count())

# Smooth the data
roll_df = pivoted_df.rolling(window=6).mean()

# Start plotting
plt.figure(figsize=(12, 7.5))
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Number of Posts', fontsize=14)
plt.ylim(0, 35000)

for column in roll_df.columns:
    plt.plot(roll_df.index, roll_df[column], label=column)

plt.legend()
plt.show()
