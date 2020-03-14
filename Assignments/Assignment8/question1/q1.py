from pmdarima import auto_arima
import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt
#Reading the datasets
historical_Data=pd.read_csv('https://media-doselect.s3.amazonaws.com/generic/MJjpYqLzv08xAkjqLp1ga1Aq/Historical_Data.csv')
historical_Data["Date"] =  pd.to_datetime(historical_Data.Date, format='%Y%m%d')
df= historical_Data.groupby("Date")["Sold_Units"].sum()
days=len(df.where(df>3).dropna())
df_count = historical_Data.groupby("Country_Code")["Sold_Units"].sum()
df_at= df_count["AT"]
historical_Data=historical_Data.set_index("Date")
df_fr=historical_Data.loc[historical_Data.index.month==8]
df_fr=df_fr.groupby("Country_Code")["Sold_Units"].sum()["FR"]
result = [days,df_fr,df_at]
result=pd.DataFrame(result)
result.to_csv('/code/output/output.csv', header=False, index=False)
