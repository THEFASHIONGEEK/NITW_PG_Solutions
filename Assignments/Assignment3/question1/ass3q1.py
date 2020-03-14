import numpy as np
import pandas as pd
import csv
df = pd.read_csv("/data/training/blackfriday.csv")
a = df.isnull().any()
c=0
b=[]
for col in df.columns:
    if a[col] == True:
        c+=1
        b.append([col])
with open("/code/output/output.csv", "w",newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        writer.writerow(str(c))
        for i in range(0,len(b)):
            writer.writerow(b[i])