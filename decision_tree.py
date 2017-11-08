# Decision Trees 
# Source : https://campus.datacamp.com/courses/kaggle-python-tutorial-on-machine-learning/predicting-with-decision-trees


# You will use the scikit-learn and numpy libraries to build your first decision tree. 
# scikit-learn can be used to create tree objects from the DecisionTreeClassifier class. 
# The methods that we will use take numpy arrays as inputs 
# and therefore we will need to create those from the DataFrame that we already have. 
# We will need the following to build a decision tree
# - target: A one-dimensional numpy array containing the target/response from the train data. (Survival in your case)
# - features: A multidimensional numpy array containing the features/predictors from the train data. (ex. Sex, Age)

import numpy as np
from sklearn import tree    # Import 'tree' from scikit-learn library

# Create the target and features numpy arrays: target, features_one
target = train["Survived"].values
features_one = train[["Pclass", "Sex", "Age", "Fare"]].values

# Fit your first decision tree: my_tree_one
my_tree_one = tree.DecisionTreeClassifier()
my_tree_one = my_tree_one.fit(features_one, target)

# One way to quickly see the result of your decision tree is to see the importance of the features that are included. 
# This is done by requesting the .feature_importances_ attribute of your tree object. 
# Another quick metric is the mean accuracy that you can compute using the .score() function with features_one and target as arguments.
print(my_tree_one.feature_importances_)
print(my_tree_one.score(features_one, target))


# PREPARE KAGGLE SUBMISSION
# To send a submission to Kaggle you need to predict the survival rates for the observations in the test set. 
# In the last exercise of the previous chapter, we created simple predictions based on a single subset. 
# Luckily, with our decision tree, we can make use of some simple functions to "generate" our answer 
# without having to manually perform subsetting.

# First, you make use of the .predict() method. You provide it the model (my_tree_one), 
# the values of features from the dataset for which predictions need to be made (test). 
# To extract the features we will need to create a numpy array in the same way as we did when training the model. 
# However, we need to take care of a small but important problem first. 
# There is a missing value in the Fare feature that needs to be imputed.

# Next, you need to make sure your output is in line with the submission requirements of Kaggle: 
# a csv file with exactly 418 entries and two columns: PassengerId and Survived. 
# Then use the code provided to make a new data frame using DataFrame(), and create a csv file using to_csv() method from Pandas.

# Impute the missing value with the median
test.Fare[152] = test.Fare.median()
print(test.Fare[152])

# Extract the features from the test set: Pclass, Sex, Age, and Fare.
test_features = test[['Pclass', 'Sex', 'Age', 'Fare']].values

# Make your prediction using the test set
my_prediction = my_tree_one.predict(test_features)

# Create a data frame with two columns: PassengerId & Survived. Survived contains your predictions
PassengerId =np.array(test["PassengerId"]).astype(int)
my_solution = pd.DataFrame(my_prediction, PassengerId, columns = ["Survived"])
print(my_solution)

# Check that your data frame has 418 entries
print(my_solution.shape)

# Write your solution to a csv file with the name my_solution.csv
my_solution.to_csv("my_solution_one.csv", index_label = ["PassengerId"])


# AVOIDING OVERFITTING
# In DecisionTreeRegressor, the depth of our model is defined by two parameters: 
# - the max_depth parameter determines when the splitting up of the decision tree stops. 
# - the min_samples_split parameter monitors the amount of observations in a bucket. 
# If a certain threshold is not reached (e.g minimum 10 passengers) no further splitting can be done.
# By limiting the complexity of your decision tree you will increase its generality and thus its usefulness for prediction.

# Create a new array with the added features: features_two
features_two = train[["Pclass","Age","Sex","Fare", "SibSp", "Parch", "Embarked"]].values

#Control overfitting by setting "max_depth" to 10 and "min_samples_split" to 5 : my_tree_two
max_depth = 10
min_samples_split = 5
my_tree_two = tree.DecisionTreeClassifier(max_depth = 10, min_samples_split = 5, random_state = 1)
my_tree_two = my_tree_two.fit(features_two, target)

#Print the score of the new decison tree
print(my_tree_two.score(features_two, target))
