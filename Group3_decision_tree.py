###################################
###################################
### CS 5593 Final Project
### Decision Tree Classifier
### Author: Rafia Bushra
### Date: 12/05/22, Fall 2022
###################################
###################################


import pandas as pd
import math
import numpy as np
import matplotlib.pyplot as plt

%matplotlib inline
plt.rcParams["figure.figsize"] = (10,8)


# Data pre-processing
#######################

data = pd.read_csv("stroke_data_2.csv")

#handling missing values
data.bmi[data.bmi.isna()] = data.bmi.mean()   #replacing missing values with the average bmi
data.smoking_status[data.smoking_status.isna()] = "never smoked"  #replacing missing values with a particular value

#Dropping the id column
data.drop("id", axis=1, inplace=True)

#Dropping "Other" category in gender column
data = data[data.gender!="Other"]

#Screating some histograms
data.hist("bmi", by="stroke")
plt.show()

data.hist("age", by="stroke")
plt.show()

data.hist("avg_glucose_level", by="stroke")
plt.show()

#Reformatting the binary columns
data.gender = data.gender.map({"Female":0, "Male":1})
data.ever_married = data.ever_married.map({"No":0, "Yes":1})
data.Residence_type = data.Residence_type.map({"Rural":0, "Urban":1})

#Converting other columns into binary columns
data.age = [0 if (x<50) else 1 for x in data.age]
data.work_type = [1 if x=="Private" else 0 for x in data.work_type]
data.avg_glucose_level = [0 if x<150 else 1 for x in data.avg_glucose_level]
data.bmi = [0 if x<21 else 1 for x in data.bmi]
data.smoking_status = [0 if x=="never smoked" else 1 for x in data.smoking_status]

#resetting index and displaying finalized data
data.reset_index(inplace=True)
data.head()



# Decision Tree Classifier
def p_log_p(val):
    """
    A function to handle log of 0
    i.e. if encountered with 0log0,
    make the value 0.
    """
    if val==0:
        plogp = 0
    else:
        plogp = val*math.log2(val)
    
    return plogp


def entropy(n, c1):
    """
    A function to calculate entropy
    of a node. This is specifically for 
    binary splits and exactly two classes
    in any split. we can make such assumptions
    because we have cleaned the data this way.
    
    n: total number of instances
    c1: number of instances belonging to 1st class
    c2: number of instances belonging to 2nd class.
    """
    
    c2 = n - c1 
    
    p1t = c1/n
    p2t = c2/n
    ent = (-1)*(p_log_p(p1t)+p_log_p(p2t))
    
    return ent


def weighted_sum(n1, e1, n2, e2):
    weight1 = n1/(n1+n2)
    weight2 = n2/(n1+n2)
    w = (weight1*e1) + (weight2*e2)
    
    return w


#impurity in parent
i_parent = entropy(len(data), data.stroke.sum()) #where class 1 is stroke and class 2 is no stroke
i_parent


def information_gain(attribute):
    """
    Information gain of an attribute.
    Here, attribute is a string which is  
    the name of the attribute for which 
    we want to find the information gain.
    """
    
    node1_yes = len(data[(data[attribute]==1) & (data.stroke==1)])
    node1_no = len(data[(data[attribute]==1) & (data.stroke==0)])
    node1 = node1_yes + node1_no
    ent1 = entropy(node1, node1_yes)
    
    node2_yes = len(data[(data[attribute]==0) & (data.stroke==1)])
    node2_no = len(data[(data[attribute]==0) & (data.stroke==0)])
    node2 = node2_yes + node2_no
    ent2 = entropy(node2, node2_yes)
    
    #impurity after splitting
    i_child = weighted_sum(node1, ent1, node2, ent2)
    
    #information gain
    infoG = i_parent - i_child
    
    return infoG


attributes = list(data.columns)[:-1]


def binary_split(parent_node, attribute):
    """
    A function to split a given node into
    two child nodes based on an attribute
    condition.
    """
    df = data.iloc[parent_node]
    node1 = df[df[attribute]==1].index.tolist()
    node2 = df[df[attribute]==0].index.tolist()
    
    return node1, node2


def test_class_label(node):
    """
    A function to test whether all instances
    in a node belong to the same class label
    or not.
    """
    df = data.iloc[node]
    if len(df.stroke.unique())==1:  #If there is only 1 class label
        return True
    else:
        return False

    
def DT_Trained():
    """A decision tree model that is to be
    trained on training data.
    The model will output a trained decision 
    tree model that can be fit to test data"""
    
    root = list(data.index)
    
    temp_attributes = attributes.copy()
    max_ig = np.array([information_gain(att) for att in temp_attributes]).argmax()
    best_split = temp_attributes.pop(max_ig)
    
    untouched_nodes = [root] #nodes that were found but haven't been worked with
    untouched_level = [best_split]   #the split level at which it was appended
    
    worked_nodes = [] #nodes that were found and have been worked with 
    
    leaf_nodes = [] #leaf nodes
    leaf_level = [] #the split level at which it terminated 
    
    levels = [] #keeping track of the split steps
    
    while len(untouched_nodes)>0: #i.e. until we run out of all the nodes to work with
        
        for (node, l) in zip(untouched_nodes, untouched_level):
            
            #removing current working node from untouched and adding it to worked nodes
            worked_nodes.append(node)
            untouched_nodes.remove(node)  
            
            #Splitting current node into 2 child nodes
            n1, n2 = binary_split(node, l)
            
            #figuring out the best split
            max_ig = np.array([information_gain(att) for att in temp_attributes]).argmax()
            best_split = temp_attributes.pop(max_ig)
            
            
            #updates
            if best_split not in levels:
                levels.append(best_split)
            
            
            
            #checking for stopping criterion
            #if we run out of attributes to split on or all class labels are same, it's a leaf node
            if (len(temp_attributes)==0) | test_class_label(n1):
                leaf_node.append(n1)
                leaf_level.append(best_split)
                break
            else:
                worked_nodes.append(n1)
            untouched_nodes.append(n2)
            untouched_level.append(best_split)
            
    return levels