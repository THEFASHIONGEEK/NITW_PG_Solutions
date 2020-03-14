import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')
#reading from the file Titanic_train.csv
df=pd.read_csv('/data/training/Titanic_train.csv')
def prepForModel(df):
    new_df = df.copy()
    new_df.Pclass = new_df.Pclass.astype("int")
    new_df.Sex = new_df.Sex.replace('male',1)
    new_df.Sex = new_df.Sex.replace('female',2)
    new_df.Embarked = new_df.Embarked.replace('S',1)
    new_df.Embarked = new_df.Embarked.replace('C',2)
    new_df.Embarked = new_df.Embarked.replace('Q',3)
    return new_df
train_cl = prepForModel(df)
train_reg = train_cl.dropna()
from sklearn.linear_model import LinearRegression
from sklearn import preprocessing
Xrcol = ['Pclass', 'Sex']
Yrcol = 'Age'
X_reg = train_reg.loc[:, Xrcol]
Y_reg = train_reg.loc[:, Yrcol]
age_lm = LinearRegression()
age_lm.fit(X_reg, Y_reg)
nan_inds = train_cl.Age.isnull().nonzero()[0]
for i in nan_inds:
    train_cl.set_value(i, 'Age', age_lm.predict(train_cl.loc[i, Xrcol].values.reshape(1, -1)))
train_cl.loc[ train_cl['Age'] <18, 'Age'] = 0
train_cl.loc[ train_cl['Age'] >=18, 'Age'] = 1
df1 = train_cl[train_cl['Survived']== 1]
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
cols = ["Age",'Pclass', 'Sex', 'SibSp', 'Parch', 'Fare'] 
X = train_cl[cols]
y = train_cl['Survived']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=2)
logreg = LogisticRegression()
logreg.fit(X_train, y_train)
y_pred = logreg.predict(X_test)
confusion_matrix = confusion_matrix(y_test,y_pred)
a=np.sum(np.diag(confusion_matrix))/np.sum(confusion_matrix)
# Creating a list of the answer
result=[len(df1[df1['Age']==0])+len(df1[df1['Age']==1]),np.sum(confusion_matrix), a*100]
result=pd.DataFrame(result)
result.to_csv('/code/output/output.csv', header=False, index=False)
