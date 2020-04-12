import numpy as np
import pandas as pd
import csv
df = pd.read_csv("/data/training/titanic.csv")
with open("/code/output/output1.csv", "w",newline='') as out:
    writer = csv.writer(out, delimiter=",")
    writer.writerow([str(np.round(df["Age"].mean(),3))])
    writer.writerow([str(np.round(df["Age"].std(),3))])
    writer.writerow([str(np.round(df["SibSp"].mean(),3))])
    writer.writerow([str(np.round(df["SibSp"].std(),3))])
    writer.writerow([str(np.round(df["Parch"].mean(),3))])
    writer.writerow([str(np.round(df["Parch"].std(),3))])
    writer.writerow([str(np.round(df["Fare"].mean(),3))])
    writer.writerow([str(np.round(df["Fare"].std(),3))])    
with open("/code/output/output2.csv", "w",newline='') as out:
    writer = csv.writer(out, delimiter=",")
    p = len(df[df['Survived']== 1])/len(df["Survived"])
    writer.writerow([str(np.round(p*100,3))])
    only_male=df[df['Sex']=='male']
    probability_male=len(only_male)/len(df)
    only_female=df[df['Sex']=='female']
    probability_female=len(only_female)/len(df)
    All_par_Age=df[df.Survived==1]
    probability_All_par_Age_male=len(All_par_Age[All_par_Age.Sex=='male'])/len(only_male)
    probability_All_par_Age_female=len(All_par_Age[All_par_Age.Sex=='female'])/len(only_female)
    writer.writerow([str(np.round(probability_All_par_Age_female,3))])
    writer.writerow([str(np.round(probability_All_par_Age_male,3))])
    df1 = df[df['Pclass']== 1]
    df2 = df[df['Pclass']== 3]
    writer.writerow([str(np.round(df1["Age"].mean()-df2["Age"].mean(),3))])
