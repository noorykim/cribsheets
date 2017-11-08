# Python


# Massage data

## Rename columns

df.rename()
```
df = df.rename({'old1':'new1'. 'old2':'new2'}, inplace=False) 
```

## Transpose data sets

[pd.melt()](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.melt.html) : change flat file to long file
```
df_melted = pd.melt(df, id_vars=['id1', 'id2'])
```


# Summarize data

## Dimensions
```
df.shape      # dimensions

df.shape[0]   # rows
len(df.shape)

df.shape[1]   # columns
```

## Frequency - 1-way table

df.groupby()
```
df_summary = df.groupby('varname').count()
```





# Key

df = dataFrame


pd = pandas

np = numpy
