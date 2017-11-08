# Python

# Import data

## Jupyter
```
%matplotlib inline        # Jupyter needs this
import matplotlib as mp
```

# Peek at data
```
df.head()            # 1st 6 rows
df.tail()            # last 6 rows
df.describe()        # max min etc
```

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

# Impute data

```
df['varname'].fillna(imputed_values)
```

# Summarize data

## Dimensions
```
df.shape      # dimensions

df.shape[0]   # rows
len(df.shape)

df.shape[1]   # columns
```

## One variable
```
df.varname.mean()
df.varname.median()
```


## Frequency - 1-way table
On a single variable
```
# absolute numbers
df["varname"].value_counts()
df_summary = df.groupby('varname').count()

# percentages
df["varname"].value_counts(normalize = True)
```

On a subset of data - note that order of subsetting vs column selection doesn't change the outcome (although runtime may be affected)
```
# Titanic : Males that survived vs males that passed away
train[train.Sex == 'male']["Survived"].value_counts()
train["Survived"][train.Sex == 'male'].value_counts()
```

## More stratified tables

[Erik Marsja](https://www.marsja.se/pandas-python-descriptive-statistics/)


# Analyze/Predict using data


# Key

df = dataFrame


pd = pandas

np = numpy
