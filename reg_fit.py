# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 10:59:04 2020

@author: smr6743
"""

from sklearn.model_selection import cross_val_score
from sklearn import linear_model
from sklearn.preprocessing import PolynomialFeatures
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
import pandas as pd

###Function that operates with two dataframe columns,
###a dictionary with varying degrees as keys and colors as the values,
###and k-folds with a default of 5
###returns a scatter plot of the data, 
###a reg fit line for each degree with it's respective score, 
###and the cross validation score for each degree


def reg_fit(x, y, degree, folds=5):
    
    x = np.array(x).reshape(-1,1)         ###Reshaping the data for the model
    y = np.array(y).reshape(-1,1)
    plt.scatter(x,y,c='b')                   ###Scatter plot of data
    
    ###iterates through degree dictionary and plots fit line with degree deg and color color
    for deg,color in degree.items():  
        reg = linear_model.LinearRegression()      ###Initzialize reg
        poly_f=PolynomialFeatures(degree=deg,include_bias=False)
        x_poly = poly_f.fit_transform(x)
        reg.fit(x_poly, y)
        ###Plot the data and the regression line
        l0=np.linspace(min(x)-1, max(x)+1, 100)
        l1=l0.reshape(-1,1)
        L1=poly_f.fit_transform(l1) 
        plt.plot(l1, reg.predict(L1), color)
        cvs=cross_val_score(reg, x_poly, y, cv=folds
                    , scoring='r2')
        print("The reg.score() is: ", reg.score(x_poly,y), " with degree" , deg, ", color = ", color, 
              " and the score from cross-folding is: ", np.mean(cvs))
        
        
iris = datasets.load_iris()
iris_df = pd.DataFrame(iris.data, columns=iris.feature_names)
petal_l = iris_df["petal length (cm)"]
petal_w = iris_df["petal width (cm)"]
reg_fit(petal_l, petal_w, {1:'k', 2:'r', 3:'g'})   