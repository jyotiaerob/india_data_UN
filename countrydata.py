import pandas as pd 
import matplotlib.pyplot as plt 
from matplotlib import style
import csv

df=pd.read_csv('C:\\Users\\PrismADS\\Desktop\\indData.csv')
df.to_csv('C:\\Users\\PrismADS\\Desktop\\newcsv2.csv')

print(df)
df.plot()
plt.show()