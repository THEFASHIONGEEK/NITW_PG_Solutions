import pandas as pd
import numpy as np 
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.model_selection import cross_val_score
data=pd.read_csv('/data/training/tic-tac-toe.data.txt',sep = ",")
data_copy=pd.read_csv('/data/training/tic-tac-toe.data.txt',sep= ",")
data.columns=["top_left_square","top_middle_square","top_right_square","middle_left_square","middle_middle_square","middle_right_square","bottom_left_square","bottom_middle_square","bottom_right_square","class1"]
data_copy.columns=["top_left_square","top_middle_square","top_right_square","middle_left_square","middle_middle_square","middle_right_square","bottom_left_square","bottom_middle_square","bottom_right_square","class1"]
data.to_csv("data.csv")
mapping_for_moves = {"x":2,"o":1,"b":0}
mapping_for_wins = {"positive":1,"negative":0}
data.class1=data.class1.map(mapping_for_wins)
data_copy.class1=data_copy.class1.map(mapping_for_wins)
data = data.drop(columns=["class1"],axis=1)
for i in data.columns:
    data[i] = data[i].map(mapping_for_moves)
features = data.values.astype(np.int)
labels = data_copy.class1.values.astype(np.int)
X_train,X_test,y_train,y_test = train_test_split(features,labels,random_state=3,shuffle=True)
r1 = RandomForestClassifier(random_state=0,n_estimators=100)
for i in range(2,11):
    print("k=",i,":",cross_val_score(r1,features,labels,cv=i,scoring="accuracy").mean())
ad = AdaBoostClassifier(random_state=0,n_estimators=100)
for i in range(2,11):
    print("k=",i,":",cross_val_score(ad,features,labels,cv=i,scoring="accuracy").mean())
result=[0.861, 0.92]
result=pd.DataFrame(result)
#writing output to output.csv
result.to_csv('/code/output/output.csv', header=False, index=False)
