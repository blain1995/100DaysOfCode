import pandas as pd
import matplotlib.pyplot as plt

#  Read in data
colours = pd.read_csv("data/colors.csv", header=0)
sets = pd.read_csv("data/sets.csv", header=0)
themes = pd.read_csv("data/themes.csv", header=0)

# Determine how many unique colours there are and how many are transparent
print(colours.name.nunique())
print(colours.value_counts("is_trans"))

# Investigate the early sets
print(sets.sort_values('year').head())
first_sets = sets[sets['year'] == 1949]

# Investigate the number of parts
print(sets.sort_values('num_parts', ascending=False).head())
sets_by_year = sets.groupby('year').count()
trimmed_data = sets_by_year.iloc[0:69,:]

# plt.plot(trimmed_data.index, trimmed_data.set_num)
# plt.show()

themes_by_year = sets.groupby('year').agg({'theme_id': pd.Series.nunique}).iloc[0:69]
themes_by_year.rename(columns={'theme_id':'nr_themes'}, inplace=True)

# # Plot line graph of number of sets and number of themes at once
# ax1 = plt.gca()
# ax2 = ax1.twinx()
#
# ax1.plot(trimmed_data.index, trimmed_data.set_num, label="number of sets per year", color='g')
# ax2.plot(themes_by_year.index, themes_by_year.nr_themes, label="number of sets per year", color='b')
#
# ax1.set_xlabel('Year')
# ax1.set_ylabel('Number of Sets', color='green')
# ax2.set_ylabel('Number of Themes', color='blue')
#
# plt.show()

## Plot scatter plot of parts per set
# parts_per_set = sets.groupby('year').agg({'num_parts': pd.Series.mean}, inplace = True)
#
# plt.scatter(parts_per_set.index[:-2], parts_per_set.num_parts[:-2])
# plt.show()

# Investigate number of sets per lego theme
set_theme_count = sets['theme_id'].value_counts()
print(set_theme_count.head())

set_theme_count = pd.DataFrame({'id': set_theme_count.index,
                                'set_count': set_theme_count.values})

merged = pd.merge(set_theme_count, themes, on='id')
plt.figure(figsize=(14,8))
plt.xticks(fontsize=14, rotation=45)
plt.yticks(fontsize=14)
plt.ylabel('Nr of Sets', fontsize=14)
plt.xlabel('Theme Name', fontsize=14)
plt.bar(merged.name[:10], merged.set_count[:10])
plt.show()
