import numpy as np
import pandas as pd
import csv
df = pd.read_csv("/data/training/blackfriday.csv")
b=[]

b.append([np.round(np.mean(df["Purchase"]),2)])

b.append([np.round(np.median(df["Purchase"]),2)])

c=[]
from collections import Counter
lst = df["Purchase"]
d_mem_count = Counter(lst)
for k in d_mem_count.keys():
    if d_mem_count[k] == max(d_mem_count.values()):
        c.append([k])
c=sorted(c)

with open("/code/output/output.csv", "w") as out:

    writer = csv.writer(out, delimiter=",")
    
    for i in range(0,len(b)):

            writer.writerow(b[i])

    for i in range(0,len(c)):

            writer.writerow(c[i])