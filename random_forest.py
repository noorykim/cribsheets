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
