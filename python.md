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


# Analyze/Predict using data

## Decision Trees
```
# Import the Numpy library
import numpy as np

# Import 'tree' from scikit-learn library
from sklearn import tree

# Print the train data to see the available features
print(train)

# Create the target and features numpy arrays: target, features_one
target = train["Survived"].values
features_one = train[["Pclass", "Sex", "Age", "Fare"]].values

# Fit your first decision tree: my_tree_one
my_tree_one = tree.DecisionTreeClassifier()
my_tree_one = my_tree_one.fit(features_one, target)

# Look at the importance and score of the included features
print(my_tree_one.feature_importances_)
print(my_tree_one.score(features_one, target))

```


# Key

df = dataFrame


pd = pandas

np = numpy
