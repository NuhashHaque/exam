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

#Correlation with output variable
cor_target = abs(cor["MEDV"])
#Selecting highly correlated features
relevant_features = cor_target[cor_target>0.5]
relevant_features


def correlation_maker(df):
    correlation = df.corr().round(2)
    plt.figure(figsize = (19,7))
    sns.heatmap(correlation, annot = True, cmap = 'YlOrBr')

def null_counter(df):
    for col in df.columns:
        print(col)
        print(df[str(col)].isnull().sum())

def categorical_converter(df):
    df['gender'] = df['gender'].replace({'M':1, 'F':0})