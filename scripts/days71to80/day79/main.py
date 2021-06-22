import pandas as pd

# Read in data
df = pd.read_csv('salaries_by_college_major.csv')
pd.options.display.float_format = '{:,.2f}'.format
print(df.shape)
print(df.columns)
print(df.isna)

# Clean dataframe
clean_df = df.dropna()
print(clean_df.shape)

# Investigate data and identify high-risk/low-risk careers
max_mc_salary = clean_df['Undergraduate Major'].loc[clean_df['Mid-Career Median Salary'].idxmax()]

risk = clean_df['Mid-Career 90th Percentile Salary'].subtract(clean_df['Mid-Career 10th Percentile Salary'])
clean_df.insert(1, 'Spread', risk)
print(clean_df.head())

low_risk = clean_df.sort_values('Spread')[['Undergraduate Major', 'Spread']].head()
high_risk = clean_df.sort_values('Spread', ascending=False)[['Undergraduate Major', 'Spread']].head()

top_potential = clean_df.sort_values('Mid-Career 90th Percentile Salary', ascending=False)
print(top_potential[['Undergraduate Major', 'Spread']].head())

# Group by the type of major (STEM, HASS etc), and find the mean of each column
print(clean_df.groupby("Group").mean())

