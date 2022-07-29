import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import math
import seaborn as sns
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.compose import make_column_transformer
from sklearn.preprocessing import OneHotEncoder
from sklearn import metrics
from utils import correlation_maker



data = pd.read_csv('./F3/Dataset/data.csv')


#Splitting Data and Label
y = data.diagnosis# M or B 

#Removing Unnecessary Columns
list = ['Unnamed: 32','id','diagnosis']



x = data.drop(list,axis = 1 )
#print(x)
print(x.describe())
correlation_maker(x)

