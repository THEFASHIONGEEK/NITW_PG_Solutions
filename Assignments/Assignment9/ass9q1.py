import pandas as pd
import numpy as np
import csv
from sklearn.preprocessing import StandardScaler
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
#Load data
df_train= pd.read_csv("/data/training/train.csv")
df_test = pd.read_csv("/data/test/test.csv")
df1 = df_train.drop(['id','Unnamed: 0','Unnamed: 32'],axis=1)
df2 = df_test.drop(['id','Unnamed: 0','Unnamed: 32'],axis=1)
x = df1.drop('diagnosis',axis=1)
y = df_train.diagnosis.map({'B' :0 ,'M' :1})
x_test = df2.drop('diagnosis',axis=1)
y_test = df_test.diagnosis.map({'B' :0 ,'M' :1})
scalar = StandardScaler()
X = scalar.fit_transform(x)
X_test = scalar.fit_transform(x_test)
model= GaussianNB()
model.fit(X,y)
y_pred1 = model.predict(X_test)
model1= LogisticRegression()
model1.fit(X,y)
y_pred2 = model1.predict(X_test)
acc1 = accuracy_score(y_test,y_pred1)
acc2 = accuracy_score(y_test,y_pred2)
#write your output in csv in this form(exactly to three decimals points)
data={round(acc1,4),round(acc2,4)}
result=pd.DataFrame(data)
result.to_csv('/code/output/output.csv', index=False,header=False)