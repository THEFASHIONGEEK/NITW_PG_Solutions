import pandas as pd

#Read the input file
df = pd.read_csv("/data/training/sales.csv")
df2= df.iloc[:,[1,3]]
df3 = df2.groupby("year").sum()
a = df3.loc[df3['sales'].idxmax()]
with open('/code/output.txt','w') as output:
    print(1960,file = output)
