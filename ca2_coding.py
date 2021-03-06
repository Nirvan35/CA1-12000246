# -*- coding: utf-8 -*-
"""CA2-coding.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cz66RATPsp-d7FCU804lhskuKaKVcLPL
"""

import pandas as pd, numpy as np
import matplotlib.pyplot as plt

# Column names to be used for training and testing sets-
col_names = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'Class']

# Read in training and testing datasets-
training_data = pd.read_csv("shuttle_train.csv", delimiter = ' ', names = col_names)
testing_data = pd.read_csv("shuttle_test.csv", delimiter = ' ', names = col_names)

# Check training data for missing values-
training_data.isnull().values.any()
## False

# Check testing data for missing values-
testing_data.isnull().values.any()
## False

from sklearn.model_selection import train_test_split
td_class_6 = training_data.Class == 6
training_data_modified = training_data.loc[~td_class_6]
X = training_data_modified.drop('Class', axis = 1)
y = training_data_modified['Class']

x_train,x_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=0)

#1) Feature Selection:

#1.1) Standardization:
from sklearn.preprocessing import StandardScaler, MinMaxScaler
sc=StandardScaler()
sc.fit(x_train,y_train)
x_train_std=sc.transform(x_train)
x_test_std=sc.transform(x_test)

#1.2) Normalization:
mms=MinMaxScaler()
mms.fit(x_train,y_train)
x_train_mms=mms.transform(x_train)
x_test_mms=mms.transform(x_test)

#2) Choosing a model:

#2.1) Perceptron:
from sklearn.linear_model import Perceptron
model_perceptron = Perceptron()
model_perceptron.fit(x_train_std,y_train)       #training for optimization
pred_train=model_perceptron.predict(x_train_std)
pred_test=model_perceptron.predict(x_test_std)
from sklearn.metrics import accuracy_score
print('Training performance=',accuracy_score(pred_train,y_train))
print('Testing performance=',accuracy_score(pred_test,y_test))

## Training performance= 0.9436689111512564
## Testing performance= 0.9400720361713542

#2.2) Logistic regression
from sklearn.linear_model import LogisticRegression
model_lr = LogisticRegression()
model_lr.fit(x_train_std,y_train)           #training for optimization
pred_train2=model_lr.predict(x_train_std)
pred_test2 = model_lr.predict(x_test_std)
from sklearn.metrics import accuracy_score
print('Training performance=',accuracy_score(pred_train2,y_train))
print('Testing performance=',accuracy_score(pred_test2,y_test))

## Training performance= 0.9676137296764658
## Testing performance= 0.9659744041689018

#2.3) Decision Tree Classifier
from sklearn.tree import DecisionTreeClassifier
model_DT = DecisionTreeClassifier()
model_DT.fit(x_train_std, y_train)               #training for optimization
pred_train3 = model_DT.predict(x_train_std)
pred_test3 = model_DT.predict(x_test_std)
from sklearn.metrics import accuracy_score
print('Training performance=',accuracy_score(pred_train3,y_train))
print('Testing performance=',accuracy_score(pred_test3,y_test))

## Training performance= 1.0
## Testing performance= 0.9995401946509311

#2.4) SVC
from sklearn.svm import SVC
model_svc = SVC()
model_svc.fit(x_train_std, y_train)                #training for optimization
pred_train4 = model_svc.predict(x_train_std)
pred_test4 = model_svc.predict(x_test_std)
from sklearn.metrics import accuracy_score
print('Training performance=',accuracy_score(pred_train4,y_train))
print('Testing performance=',accuracy_score(pred_test4,y_test))

## Training performance= 0.9982591558548202
## Testing performance= 0.9977776074795004

"""We will use **Decision Tree Classifier** since it has the highest accuracy score for both *training and testing* for preparing **Confusion Matrix.** 
So, we will be using the variable **pred_test3** and **model_DT**.
"""

#3) Confusion Matrix with Confusion Matrix Plot
from sklearn.metrics import confusion_matrix
matrix = confusion_matrix(pred_test3,y_test)
print(matrix)

[[10191     0     0     0     0     0]
 [    1    11     0     0     0     0]
 [    0     0    43     0     0     0]
 [    3     0     2  2065     0     0]
 [    0     0     0     0   731     0]
 [    0     0     0     0     0     2]]

from sklearn.metrics import plot_confusion_matrix
plot_confusion_matrix(model_DT,x_test_std,y_test)

## for confusion matrix plot, refer to coding on Google Colab ##

#4) Prediction on unknown data

#4.1) Using Predict() function with Decision Trees
from sklearn.tree import DecisionTreeRegressor
model_DTR = DecisionTreeRegressor(max_depth=5).fit(x_train,y_train)
DT_predict = model_DTR.predict(x_test) #Predictions on Testing data
print(DT_predict)

## [1.0020645 4.        1.0020645 ... 1.0020645 1.0020645 1.       ]

#4.2) Using Predict() function with KNN
from sklearn.neighbors import KNeighborsRegressor
KNN_model = KNeighborsRegressor(n_neighbors=3).fit(x_train,y_train)

## [1. 4. 1. ... 1. 1. 1.]
KNN_predict = KNN_model.predict(x_test) #Predictions on Testing data
print(KNN_predict)
