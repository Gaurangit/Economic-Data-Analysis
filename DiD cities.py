import pandas as pd
import csv
import numpy as np
import os
from os.path import expanduser

inp="CleanResults/UradDal/M_Margin_monthly(monthwise)_UradDal.xlsx.csv"
klo="DiD_UradDal_monthly(monthwise)M.xlsx.csv"
Selected_cities=["Dharwad", 'Mysore', 'Hyderabad', 'Karimnagar', 'Vijaywada', 'Visakhapatnam', 'Warangal']


data = pd.read_csv(inp)
df = pd.DataFrame(data)


colnm=['Month', 'Region', 'Margin']
k=len(df['Month No.'])

Selected_c=[]
for ci in Selected_cities:
    if ci in list(df.columns):
        Selected_c.append(ci)

arr=np.zeros((0,3))
lst = []
for city in Selected_c:
    
    b=df[city]
    for a in range(k):
        lst.append([1+a, city, b[a]])
        
df1 = pd.DataFrame(lst, columns=colnm)
df1

df1.to_csv( klo, index=False)
