# Author: Tate Smith - University of Oklahoma
# Class: CS 5033
# Date: 12/16/21

import random
import numpy as np
import matplotlib.pyplot as plt
import math



# Prepare the data
data = np.genfromtxt("train_strokes.txt", delimiter=',', max_rows=100000)

'''
closeData = data[1:,4]
percentageChanges = np.zeros(np.size(closeData))
index = 1
for close in closeData[0:-1]:
    percentageChanges[index - 1] = 100 * (closeData[index] - closeData[index - 1]) / closeData[index - 1]
    index += 1

num_feature_days = 10
remainder = np.size(percentageChanges) % (num_feature_days + 1)

numRows = np.size(percentageChanges[0:-remainder]) // (num_feature_days + 1)

shapedData = percentageChanges[0:-remainder].reshape(numRows, num_feature_days + 1)
if remainder == 0:
    numRows = np.size(percentageChanges) // (num_feature_days + 1)

    shapedData = percentageChanges.reshape(numRows, num_feature_days + 1)
'''
shapedData = data
n = np.size(shapedData[:,0])
n_train = int(n*0.9)
n_test = int(n*0.1)

trainingData = shapedData[0:n_train,:]
testingData = shapedData[n - n_test:,:]

#All feature vectors
#X_training = trainingData[:,0:-1] #feature data (training)
#X_testing = testingData[:,0:-1] #feature data (testing)

Y_training = trainingData[:,-1] #label vector (training)
Y_testing = testingData[:,-1] #label vector (testing)

#Only age column
X_training = trainingData[:,2:4] #feature data (training)
X_testing = testingData[:,2:4] #feature data (testing)

max_neighbors = 30
MSEs = []
percent_correct_direction_predictions_arr = []
for i in range(max_neighbors):
    num_neighbors = i
    predictions = np.zeros(n_test)

    for x in range(len(testingData)):
        euclidian_distances = np.sqrt(np.sum((X_training - X_testing[x]) ** 2, axis=1))
        predictions[x] = Y_training[np.argsort(euclidian_distances, axis=0)[:num_neighbors]].mean()

    num_correct_direction_predictions = 0
    predIndex = 0
    for pred in predictions:
        #if pred * Y_testing[predIndex] > 0:
        if (pred > 0.5 and Y_testing[predIndex] > 0.5) or (pred < 0.5 and Y_testing[predIndex] < 0.5):
            num_correct_direction_predictions += 1
        predIndex += 1
    percent_correct_direction_predictions = num_correct_direction_predictions / len(predictions)
    percent_correct_direction_predictions_arr.append(percent_correct_direction_predictions)
    MSE = ((predictions - Y_testing) ** 2).mean()
    # print(percent_correct_direction_predictions)
    MSEs.append(MSE)

plt.plot(range(max_neighbors), MSEs)
plt.xlabel("Number of Neighbors")
plt.ylabel("Mean Squared Error")
plt.show()

plt.plot(range(max_neighbors), percent_correct_direction_predictions_arr, color="red", label="Accuracy %")
plt.xlabel("Number of Neighbors")
plt.ylabel("Accuracy %")
plt.show()
