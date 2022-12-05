# Author: Tate Smith - University of Oklahoma

import random
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import MinMaxScaler
import math


def knn_accuracy_testing(k):
    # Prepare the data
    # data = np.genfromtxt("healthcare-dataset-stroke-data.txt", delimiter=',', max_rows=100000)
    df = pd.read_table("train_strokes.txt", delimiter=',', header=0)

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
    # df = pd.DataFrame(data, columns = ['id','gender','age','hypertension','heart_disease','ever_married','work_type','Residence_type','avg_glucose_level','bmi','smoking_status','stroke'])
    print(df.columns)
    print(df.to_numpy()[1])
    df['bmi'].fillna(df['bmi'].mean(), inplace=True)

    df['gender'] = df['gender'].eq('Male').mul(1)
    df.ever_married = df.ever_married.eq('Yes').mul(1)
    df.Residence_type = df.Residence_type.eq('Urban').mul(1)
    '''
    df['work_type']=df['work_type'].astype('category')
    df['work_new'] = df['work_type'].cat.codes

    df['smoking_status']=df['smoking_status'].astype('category')
    df['smoke_new'] = df['smoking_status'].cat.codes

    enc=OneHotEncoder()
    enc_data=pd.DataFrame(enc.fit_transform(df[['work_new','smoke_new']]).toarray())
    '''
    one_hot_encoded_data = pd.get_dummies(df, columns=['work_type', 'smoking_status'])
    print(one_hot_encoded_data)

    shapedData = one_hot_encoded_data.to_numpy()
    print(shapedData)
    n = np.size(shapedData[:, 0])
    n_train = int(n * 0.9)
    n_test = int(n * 0.1)

    trainingData = shapedData[0:n_train, :]
    testingData = shapedData[n - n_test:, :]

    # All feature vectors
    X_training = trainingData[:, 1:-1]  # feature data (training)
    X_testing = testingData[:, 1:-1]  # feature data (testing)
    print(X_training[0])

    scaler = MinMaxScaler(feature_range=(0, 1))
    X_training = scaler.fit_transform(X_training)
    X_testing = scaler.fit_transform(X_testing)
    print(X_training[0])
    X_training[:, 1] *= 10
    X_testing[:, 1] *= 10

    print(X_training[0])

    Y_training = trainingData[:, -1]  # label vector (training)
    Y_testing = testingData[:, -1]  # label vector (testing)

    # Only age column
    # X_training = trainingData[:,2:4] #feature data (training)
    # X_testing = testingData[:,2:4] #feature data (testing)

    max_neighbors = k
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
            # if pred * Y_testing[predIndex] > 0:
            if (pred > 0.05 and Y_testing[predIndex] > 0.5) or (pred <= 0.05 and Y_testing[predIndex] < 0.5):
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


def knn_single_prediction(k, input_record, datasetfile):
    # Prepare the data
    df = pd.read_table(datasetfile, delimiter=',', header=0)

    # append the input record to the data frame, so we clean it in the same way as the dataset
    input_record.append(0)
    df.loc[len(df.index)] = input_record

    ########################
    # Data cleaning
    ########################

    # Fill missing values in bmi (less than 0.5% of records)
    df['bmi'].fillna(df['bmi'].mean(), inplace=True)

    # convert string attributes to binary
    df['gender'] = df['gender'].eq('Male').mul(1)
    df.ever_married = df.ever_married.eq('Yes').mul(1)
    df.Residence_type = df.Residence_type.eq('Urban').mul(1)
    '''
    df['work_type']=df['work_type'].astype('category')
    df['work_new'] = df['work_type'].cat.codes

    df['smoking_status']=df['smoking_status'].astype('category')
    df['smoke_new'] = df['smoking_status'].cat.codes

    enc=OneHotEncoder()
    enc_data=pd.DataFrame(enc.fit_transform(df[['work_new','smoke_new']]).toarray())
    '''
    # convert categorical data to separate columns of 0 or 1 (one hot encoding)
    one_hot_encoded_data = pd.get_dummies(df, columns=['work_type', 'smoking_status'])
    # print(one_hot_encoded_data)

    shapedData = one_hot_encoded_data.to_numpy()
    # print(shapedData)
    n = np.size(shapedData[:, 0])
    # n_train = int(n * 0.9)
    # n_test = int(n * 0.1)

    trainingData = shapedData

    # All feature vectors
    X_training = trainingData[:, 1:-1]  # feature data (training)
    # print(X_training[0])

    scaler = MinMaxScaler(feature_range=(0, 1))
    X_training = scaler.fit_transform(X_training)
    # print(X_training[0])
    X_training[:, 1] *= 10

    X_input_record_cleaned = X_training[-1]
    X_training = X_training[0:-1]

    # print(X_training[0])

    Y_training = trainingData[:-1, -1]  # label vector (training)

    euclidian_distances = np.sqrt(np.sum((X_training - X_input_record_cleaned) ** 2, axis=1))
    prediction = Y_training[np.argsort(euclidian_distances, axis=0)[:k]].mean()

    if prediction > 0.005:
        return True
    else:
        return False
