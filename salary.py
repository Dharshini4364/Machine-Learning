# -*- coding: utf-8 -*-
"""Salary.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1SVgKe80SFHqMTvRKcHQhr7c64YBywYTk
"""

import pandas as pd
from sklearn.linear_model import LinearRegression

saldf=pd.read_csv('/content/Salary Data.csv')

saldf.head(10)

LR=LinearRegression()

saldf.isnull().sum()

saldf.info()

saldf.dropna(inplace=True)

saldf.isnull().sum()

saldf.info()

a=saldf[['Years of Experience']]
b=saldf['Salary']

LR.fit(a,b)

from sklearn.preprocessing import LabelEncoder
LE=LabelEncoder()

saldf['gen']=LE.fit_transform(saldf['Gender'])

saldf.head()

LE1=LabelEncoder()
saldf['Edu']=LE1.fit_transform(saldf['Education Level'])
saldf.head()

LE2=LabelEncoder()
saldf['Job']=LE2.fit_transform(saldf['Job Title'])
saldf.head()

c=saldf[['Age','gen','Edu','Job','Years of Experience']]

d=saldf['Salary']

LR1=LinearRegression()

LR1.fit(c,d)

LR1.predict([[25,1,1,1,3]])