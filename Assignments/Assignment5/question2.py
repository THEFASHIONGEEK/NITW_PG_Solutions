import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')
#reading from the file Titanic_train.csv
df=pd.read_csv('/data/training/Titanic_train.csv')
#view the dataset
index = df['Age'].index[df['Age'].apply(np.isnan)]
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
a= []
for i in nan_inds:
    train_cl.set_value(i, 'Age', age_lm.predict(train_cl.loc[i, Xrcol].values.reshape(1, -1)))
    a.append(age_lm.predict(train_cl.loc[i, Xrcol].values.reshape(1, -1)))
result=[df['Age'].isna().sum(),sum(df['Age'].index[df['Age'].apply(np.isnan)]),np.mean(a)]
result=pd.DataFrame(result)
# writing output to output.csv
result.to_csv('/code/output/output.csv', header=False, index=False)
