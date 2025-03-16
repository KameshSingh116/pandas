# pandas
Learning Pandas
proceeding....
loading....


df.fillna(df.mean(), inplace=True) → Fills all numeric columns with their mean.
df.fillna(df.median(), inplace=True) → Fills with the median.
df.fillna(df.mode().iloc[0], inplace=True) → Fills with the mode.