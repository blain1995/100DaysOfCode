# Load in packages
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

#  Import data
df_tesla = pd.read_csv("data/TESLA Search Trend vs Price.csv")
df_unemployment = pd.read_csv("data/UE Benefits Search vs UE Rate 2004-19.csv")
df_btc_search = pd.read_csv("data/Bitcoin Search Trend.csv")
df_btc_price = pd.read_csv("data/Daily Bitcoin Price.csv")

# Inspect Tesla dataframe
print(f"The dataframe has {df_tesla.shape[0]} rows and {df_tesla.shape[1]} columns.\n"
      f"The column names are {df_tesla.columns.values}.\n"
      f"The largest value in the {df_tesla.columns.values[1]} is {df_tesla[df_tesla.columns.values[1]].max()}.\n"
      f"The smallest value in the {df_tesla.columns.values[1]} is {df_tesla[df_tesla.columns.values[1]].min()}.\n\n"
      f"A summary of the data can be found here:\n"
      f"{df_tesla.describe()}\n\n")

# Inspect the unemployment dataframe
print(f"The dataframe has {df_unemployment.shape[0]} rows and {df_unemployment.shape[1]} columns.\n"
      f"The column names are {df_unemployment.columns.values}.\n"
      f"The largest value in the {df_unemployment.columns.values[1]} is "
      f"{df_unemployment[df_unemployment.columns.values[1]].max()}.\n"
      f"The smallest value in the {df_unemployment.columns.values[1]} is "
      f"{df_unemployment[df_unemployment.columns.values[1]].min()}.\n\n"
      f"A summary of the data can be found here:\n"
      f"{df_unemployment.describe()}\n\n")

# Inspect the bitcoin dataframes
print(f"The dataframe has {df_btc_search.shape[0]} rows and {df_btc_search.shape[1]} columns.\n"
      f"The column names are {df_btc_search.columns.values}.\n"
      f"The largest value in the {df_btc_search.columns.values[1]} is "
      f"{df_btc_search[df_btc_search.columns.values[1]].max()}.\n"
      f"The smallest value in the {df_btc_search.columns.values[1]} is "
      f"{df_btc_search[df_btc_search.columns.values[1]].min()}.\n\n"
      f"A summary of the data can be found here:\n"
      f"{df_btc_search.describe()}\n\n")

print(f"The dataframe has {df_btc_price.shape[0]} rows and {df_btc_price.shape[1]} columns.\n"
      f"The column names are {df_btc_price.columns.values}.\n"
      f"The largest value in the {df_btc_price.columns.values[1]} is "
      f"{df_btc_price[df_btc_price.columns.values[1]].max()}.\n"
      f"The smallest value in the {df_btc_price.columns.values[1]} is "
      f"{df_btc_price[df_btc_price.columns.values[1]].min()}.\n\n"
      f"A summary of the data can be found here:\n"
      f"{df_btc_price.describe()}\n")

# Identify which dataframes have missing values
print(f"The Tesla dataframe has {df_tesla.isna().values.sum()} missing values,\n"
      f"the unemployment dataframe has {df_unemployment.isna().values.sum()} missing values,\n"
      f"and finally the bitcoin dataframes have {df_btc_search.isna().values.sum()} and "
      f"{df_btc_price.isna().values.sum()} missing values")

df_btc_price.dropna(inplace=True)

# Convert dates to datetime values for each dataframe
df_tesla.MONTH = pd.to_datetime(df_tesla.MONTH)
df_unemployment.MONTH = pd.to_datetime(df_unemployment.MONTH)
df_btc_search.MONTH = pd.to_datetime(df_btc_search.MONTH)
df_btc_price.DATE = pd.to_datetime(df_btc_price.DATE)

# Make the bitcoin price and search volume comparable
df_btc_price_monthly = df_btc_price.resample('M', on='DATE').last()


years = mdates.YearLocator()
months = mdates.MonthLocator()
years_fmt = mdates.DateFormatter('%Y')

# Plot the Tesla data
fig = plt.figure(figsize=(13,7), dpi=120)
plt.title('Tesla Web Search vs Price', fontsize=18)

ax1 = plt.gca()
ax2 = ax1.twinx()

ax1.set_ylabel('TSLA Search Trend', color='#E6232E', fontsize=14)
ax2.set_ylabel('TSLA Stock Price', color='skyblue', fontsize=14)

ax1.set_ylim([0,600])
ax1.set_xlim([df_tesla.MONTH.min(), df_tesla.MONTH.max()])

ax1.xaxis.set_major_locator(years)
ax1.xaxis.set_major_formatter(years_fmt)
ax1.xaxis.set_minor_locator(months)

ax1.plot(df_tesla.MONTH, df_tesla.TSLA_WEB_SEARCH, color='#E6232E', linewidth=3)
ax2.plot(df_tesla.MONTH, df_tesla.TSLA_USD_CLOSE, color='skyblue', linewidth=3)

for label in ax1.xaxis.get_ticklabels():
    label.set_rotation(45)
    label.set_fontsize(14)

plt.show()

# # Plot the bitcoin data
fig = plt.figure(figsize=(13,7), dpi=120)
plt.title('Bitcoin News Search vs Resampled Price', fontsize=18)
plt.xticks(fontsize=14, rotation=45)

ax1 = plt.gca()
ax2 = ax1.twinx()

ax1.set_ylabel('BTC Price', color='#F08F2E', fontsize=14)
ax2.set_ylabel('BTC Search Trend', color='skyblue', fontsize=14)

ax1.set_ylim(bottom=0,top=15000)
ax1.set_xlim([df_btc_price_monthly.index.min(), df_btc_price_monthly.index.max()])

ax1.xaxis.set_major_locator(years)
ax1.xaxis.set_major_formatter(years_fmt)
ax1.xaxis.set_minor_locator(months)

ax1.plot(df_btc_price_monthly.index, df_btc_price_monthly.CLOSE, color='#F08F2E', linewidth=3, linestyle='--')
ax2.plot(df_btc_price_monthly.index, df_btc_search.BTC_NEWS_SEARCH, color='skyblue', linewidth=3, marker='o')

plt.show()

# Plot the unemployment data
print(df_unemployment.head())
fig = plt.figure(figsize=(13,7), dpi=120)
plt.title('Monthly Search of "Unemployment Benefits" in the U.S. vs the U/E Rate', fontsize=18)
plt.xticks(fontsize=14, rotation=45)

ax1 = plt.gca()
ax2 = ax1.twinx()

ax1.set_ylabel('FRED U/E Rate', color='purple', fontsize=14)
ax2.set_ylabel('BTC Search Trend', color='skyblue', fontsize=14)

ax1.set_xlim([df_unemployment.MONTH.min(), df_unemployment.MONTH.max()])
ax1.grid(linestyle='--')

ax1.xaxis.set_major_locator(years)
ax1.xaxis.set_major_formatter(years_fmt)
ax1.xaxis.set_minor_locator(months)

ax1.plot(df_unemployment.MONTH, df_unemployment.UNRATE, color='purple', linewidth=3, linestyle='--')
ax2.plot(df_unemployment.MONTH, df_unemployment.UE_BENEFITS_WEB_SEARCH, color='skyblue', linewidth=3)

plt.show()
