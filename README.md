# pandas
Learning Pandas
proceeding....
loading....

#Mean Mode Median
df.fillna(df.mean(), inplace=True) → Fills all numeric columns with their mean.
df.fillna(df.median(), inplace=True) → Fills with the median.
df.fillna(df.mode().iloc[0], inplace=True) → Fills with the mode.

Method	Description
df.fillna(0)	Replace NaN with 0.
df.fillna(df.mean())	Replace NaN with column mean.
df.fillna(df.median())	Replace NaN with column median.
df.fillna(df.mode().iloc[0])	Replace NaN with mode.
df.fillna(method='ffill')	Fill using previous row value.
df.fillna(method='bfill')	Fill using next row value.