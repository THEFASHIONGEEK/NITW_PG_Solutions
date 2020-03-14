import pandas as pd
import matplotlib.pyplot as plt
#reading from the file Titanic_train.csv
df=pd.read_csv('/data/training/Titanic_train.csv')
#view the dataset
df1 = df[df['Survived']== 1]
df2 = df[df['Survived']== 0]
# Creating a list of the answer
result=[len(df1[df1['Pclass']==3]),len(df2[df2['Sex']== 'male']),len(df1[df1['Embarked']=='S'])]
# NOTE: Here, 100, 200 and 300 are the answer of 1st, 2nd and 3rd question respectively. Change it accordingly.

# Finally create a dataframe of the final output  and write the output to output.csv

result=pd.DataFrame(result)
# writing output to output.csv
result.to_csv('/code/output/output.csv', header=False, index=False)
