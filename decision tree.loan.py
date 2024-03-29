# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 23:30:58 2024

@author: shrey
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
## import os - Not required
from sklearn import tree, metrics
## Get the Data
loans = pd.read_csv("C:\\Users\\MY PC\\Desktop\\Desktop\\Folders\\Datascience development\\python\\Machine Learning\\decision Tree\\loan_data.csv")
loans.head()
loans.info()
loans.describe()
##Create a histogram of two FICO distributions on top of each other, one for each credit.policy outcome.
plt.figure(figsize=(10,6))
loans[loans['credit.policy']==1]['fico'].hist(alpha=0.5,color='blue',
                                              bins=30,label='Credit.Policy=1')
loans[loans['credit.policy']==0]['fico'].hist(alpha=0.5,color='red',
                                              bins=30,label='Credit.Policy=0')
plt.legend()
plt.xlabel('FICO')
##Create a similar figure, except this time select by the not.fully.paid column.
plt.figure(figsize=(10,6))
loans[loans['not.fully.paid']==1]['fico'].hist(alpha=0.5,color='blue',
                                              bins=30,label='not.fully.paid=1')
loans[loans['not.fully.paid']==0]['fico'].hist(alpha=0.5,color='red',
                                              bins=30,label='not.fully.paid=0')
plt.legend()
plt.xlabel('FICO')

## Create a countplot using seaborn showing the counts of loans by purpose, with the color hue defined by not.fully
plt.figure(figsize=(11,7))
sns.countplot(x='purpose',hue='not.fully.paid',data=loans,palette='Set1')

### see the trend between FICO score and interest rate
sns.jointplot(x='fico',y='int.rate',data=loans,color='purple')

### Create the following lmplots to see if the trend differed between not.fully.paid and credit.policy. 
plt.figure(figsize=(11,7))
sns.lmplot(y='int.rate',x='fico',data=loans,hue='credit.policy',
           col='not.fully.paid',palette='Set1')

# Setting up the Data
loans.info()

## Categorical Features


## Create a list of 1 element containing the string 'purpose'. Call this list cat_feats.
cat_feats = ['purpose']
cat_feats
final_data = pd.get_dummies(loans,columns=cat_feats,drop_first=True)
final_data
final_data.info()
## Train Test Split
from sklearn.model_selection import train_test_split

X = final_data.drop('not.fully.paid',axis=1)
X
y = final_data['not.fully.paid']
y
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=101)

## Training a Decision Tree Model
from sklearn.tree import DecisionTreeClassifier

### Create an instance of DecisionTreeClassifier() called dtree and fit it to the training data.
dtree = DecisionTreeClassifier()
dtree.fit(X_train,y_train)

## Predictions and Evaluation of Decision Tree
predictions = dtree.predict(X_test)
predictions
from sklearn.metrics import classification_report,confusion_matrix
 
print(confusion_matrix(y_test,predictions))
print(classification_report(y_test,predictions))

### Misclassified

count_misclassified = (y_test != predictions).sum()
print('Misclassified samples: {}'.format(count_misclassified))
accuracy = metrics.accuracy_score(y_test, predictions)
print('Accuracy: {:.2f}'.format(accuracy))

## Training the Random Forest model
##Create an instance of the RandomForestClassifier class and fit it to our training data from the previous step
from sklearn.ensemble import RandomForestClassifier
rfc = RandomForestClassifier(n_estimators=500)
rfc.fit(X_train,y_train)

## Predictions and Evaluation
predictions = rfc.predict(X_test)

from sklearn.metrics import classification_report,confusion_matrix
print(classification_report(y_test,predictions))

print(confusion_matrix(y_test,predictions))

### Misclassified

count_misclassified = (y_test != predictions).sum()
print('Misclassified samples: {}'.format(count_misclassified))
accuracy = metrics.accuracy_score(y_test, predictions)
print('Accuracy: {:.2f}'.format(accuracy))