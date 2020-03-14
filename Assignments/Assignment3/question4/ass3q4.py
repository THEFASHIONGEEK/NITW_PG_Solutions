import pandas as pd

import numpy as np

import csv
df = pd.read_csv("/data/training/blackfriday.csv",sep=",")

b=[]

c=0

q1 = df["Purchase"].quantile(0.25)

q3 = df["Purchase"].quantile(0.75)

iqr = q3-q1 #Interquartile range

b.append([np.round(iqr,1)])

fence_low  = q1-1.5*iqr

fence_high = q3+1.5*iqr

for col_name in range(0,len(df["Purchase"])):

    if(df.iloc[col_name]["Purchase"] < fence_low) or (df.iloc[col_name]["Purchase"] > fence_high):

        c+=1

b.append([c])

with open("/code/output/output.csv", "w") as out:

    writer = csv.writer(out, delimiter=",")

    for i in range(0,len(b)):

        writer.writerow(b[i])