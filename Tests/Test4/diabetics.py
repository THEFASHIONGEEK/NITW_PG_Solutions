import pandas as pd
import numpy as np 
train=pd.read_csv('/data/training/diabetes_train.csv')
test=pd.read_csv('/data/test/diabetes_test.csv')
train_copy = train.copy()
X_train = train.drop("Outcome",axis=1)
y_train = train_copy.Outcome
test_copy = test.copy()
X_test = test.drop("Outcome",axis=1)
y_test = test_copy.Outcome
from sklearn.ensemble import AdaBoostClassifier
from sklearn.model_selection import GridSearchCV
import xgboost as xgb
from sklearn.metrics import confusion_matrix ,accuracy_score
param_test ={"learning_rate":[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1],"n_estimators":[50,100,150,200,250,300]
alg1 = xgb.XGBClassifier()
clf1 = GridSearchCv(alg1,param_test)
clf1.fit(X_train,y_train)
alg2  = AdaBoostClassifier()
clf2 = GridSearchCv(alg2,param_test)
clf2.fit(X_train,y_train)
a =clf1.best_params_
pred1 =clf1.predict(X_test)
pred2 =clf2.predict(X_test)
c1 = confusion_matrix(y_test,pred1)
c2 = confusion_matrix(y_test,pred2)
b = round(accuracy_score(y_test,pred1)*100,2)
c =round(c1[0][0]/(c1[0][0]+c1[0][1]) *100,2)
d =round(c1[1][1]/(c[1][0]+c[1][1]) *100,2)
result=[a["learning_rate"],a["n_estimators"],b,c,d]
result=pd.DataFrame(result)
result.to_csv('/code/output/output.csv', header=False, index=False)
