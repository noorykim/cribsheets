# A Random Forest analysis in Python

# In layman's terms, the Random Forest technique handles the overfitting problem you faced with decision trees. 
# It grows multiple (very deep) classification trees using the training set. 
# At the time of prediction, each tree is used to come up with a prediction and every outcome is counted as a vote. 
# For example, if you have trained 3 trees with 2 saying a passenger in the test set will survive and 1 says he will not, 
# the passenger will be classified as a survivor. 
# This approach of overtraining trees, but having the majority's vote count as the actual classification decision, avoids overfitting.

# Building a random forest in Python looks almost the same as building a decision tree; so we can jump right to it. 
# There are two key differences, however. 
# Firstly, a different class is used. And second, a new argument is necessary. 
# Also, we need to import the necessary library from scikit-learn.

# Use RandomForestClassifier() class instead of the DecisionTreeClassifier() class.
# n_estimators needs to be set when using the RandomForestClassifier() class. 
# This argument allows you to set the number of trees you wish to plant and average over.

from sklearn.ensemble import RandomForestClassifier
features_forest = train[["Pclass", "Age", "Sex", "Fare", "SibSp", "Parch", "Embarked"]].values

# Building and fitting my_forest
forest = RandomForestClassifier(max_depth = 10, min_samples_split=2, n_estimators = 100, random_state = 1)
my_forest = forest.fit(features_forest, target)

# Print the score of the fitted random forest
print(my_forest.score(features_forest, target))

# Compute predictions on our test set features then print the length of the prediction vector
test_features = test[["Pclass", "Age", "Sex", "Fare", "SibSp", "Parch", "Embarked"]].values
pred_forest = my_forest.predict(test_features)
print(len(pred_forest))


#Request and print the `.feature_importances_` attribute
print(my_tree_two.feature_importances_)
print(my_forest.feature_importances_)

#Compute and print the mean accuracy score for both models
print(my_tree_two.score(features_two, target))
print(my_forest.score(features_two, target))
