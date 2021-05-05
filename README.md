# CA2-12000246
This is the code for Nirvan Gurung, for the purpose of CA2.

Before beginning with our coding and analysis of the coding, let us first discuss a bit about the dataset used in this report. The dataset for my report is that of Statlog (Shuttle). According to the description, this dataset should only be tackled by train/test, both the train file as well as test file is available in the link given below.

Link of dataset: https://archive.ics.uci.edu/ml/datasets/Statlog+%28Shuttle%29

NUMBER OF ATTRIBUTES
	9

In the dataset there are 9 attributes and class 1 variables and all the data are numeric in nature. The last column is the class which has been 
coded as follows :
        1       Rad Flow
        2       Fpv Close
        3       Fpv Open
        4       High
        5       Bypass
        6       Bpv Close
        7       Bpv Open
        
Approximately 80% of the data belongs to class 1.

We will be using mainly two types of data in this report, one is shuttle.trn (training data) and the other is shuttle.tst (testing data). We will also be performing the following functions on the dataset: 

1.	Feature Scaling/ Feature Identification
2.	Choosing a model
3.	Training for optimization
4.	Evaluating (highest accuracy with confusion matrix)
5.	Hyperparameter tuning
6.	Prediction on unknown data.
