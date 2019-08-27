import pandas as pd
import csv
import numpy as np
import os
from os.path import expanduser

file_name="Gur.xlsx.csv"

inp="Wholesale/"+ file_name
inp2="Retail/price_data_folder/"+ file_name


os.makedirs(os.getcwd() + '/CleanResults/'+ file_name[0:-9])


data = pd.read_csv(inp)
df = pd.DataFrame(data)
arW=df.values

datar = pd.read_csv(inp2)
df1 = pd.DataFrame(datar)
arR=df1.values

Month_avgarr= np.zeros((0,102))
city_names=[]
for row in df:
    city_names.append(row)

del city_names[0:5]

for k in range (len(city_names)):


    Month_avg=[]
    dta=[]
    a=0
    dates=list(arW[:,1])
    city=list(arW[:,5+k])

    premon='10-01'
    for i in range (len(dates)):
        date=dates[i]
        month=date[2:7]

        if month == premon:

            if date == dates[-1]:
                dta.append(city[i])
                dta=[x for x in dta if x > 0]

                try:
                    Month_avg.append(sum(dta)/len(dta))

                except ZeroDivisionError:
                    Month_avg.append(0)
                    k=0


            else:
                dta.append(city[i]) 

        else:

            premon=month

            dta=[x for x in dta if x > 0]

            try:
                Month_avg.append(sum(dta)/len(dta))

            except ZeroDivisionError:
                Month_avg.append(0)
                k=0

            dta=[city[i]]

    Month_avgarr=np.vstack((Month_avgarr,Month_avg))
    #print(len(Month_avg))

Month_avgarr=Month_avgarr.T

ghtW = pd.DataFrame(Month_avgarr, columns=city_names)
ghtW.insert(0, 'Month No.', [x+1 for x in range(102)])


ghtW.to_csv("W_mon_avg" + file_name, index=False)


Month_avgarr= np.zeros((0,102))
city_names=[]
for row in df1:
    city_names.append(row)

del city_names[0:5]

for k in range (len(city_names)):


    Month_avg=[]
    dta=[]
    a=0
    dates=list(arR[:,1])
    city=list(arR[:,5+k])

    premon='10-01'
    for i in range (len(dates)):
        date=dates[i]
        month=date[2:7]

        if month == premon:

            if date == dates[-1]:
                dta.append(city[i])
                dta=[x for x in dta if x > 0]

                try:
                    Month_avg.append(sum(dta)/len(dta))

                except ZeroDivisionError:
                    Month_avg.append(0)
                    k=0


            else:
                dta.append(city[i]) 

        else:

            premon=month

            dta=[x for x in dta if x > 0]

            try:
                Month_avg.append(sum(dta)/len(dta))

            except ZeroDivisionError:
                Month_avg.append(0)
                k=0

            dta=[city[i]]

    Month_avgarr=np.vstack((Month_avgarr,Month_avg))
    #print(len(Month_avg))

Month_avgarr=Month_avgarr.T
#city_names.insert(0, '0')
ghtR = pd.DataFrame(Month_avgarr, columns=city_names)
ghtR.insert(0, 'Month No.', [x+1 for x in range(102)])




ghtR.to_csv("R_mon_avg_" + file_name, index=False)




#######   Monthly difference datewise
#######   ...........................

city_diff=np.zeros((0,102))    


city_names=[]                              ##common city list
for row in df:                              ##
    city_names.append(row)
del city_names[0:5]

city_names2=[]
for row in df1:
    city_names2.append(row)
del city_names2[0:5]


qp=[]


for ele in city_names2 or ele in city_names:
    
    if ele  in city_names2 and ele  in city_names:
        qp.append(ele)


i=range(len(city_names))                    ##dict of cities
ct = dict(zip(city_names, i))
    
    
i=range(len(city_names2))                   ##dict of cities
ct2 = dict(zip(city_names2, i))        

        
        

for cty in qp:
    
    c=ct[cty]
    c2=ct2[cty]
    
    dw = dict(zip(arW[:,1], [x/100 for x in arW[:,5+c]]))
    dr = dict(zip(arR[:,1], arR[:,5+c2]))
    
    Month_avg=[]
    diff=[]

    premon='10-01'
    for date in list(arW[:,1]):
        if date in list(arR[:,1]):
            
            month=date[2:7]
            if month == premon:

                if date == '2018-06-24':                           ###### BE careful here with the dates and last date
                    diff.append(dr[date]-dw[date])
                    diff=[x for x in diff if x > 0]

                    try:
                        Month_avg.append(sum(diff)/len(diff))

                    except ZeroDivisionError:
                        Month_avg.append(0)
                        k=0


                else:
                    diff.append(dr[date]-dw[date])

            else:

                premon=month

                diff=[x for x in diff if x > 0]

                try:
                    Month_avg.append(sum(diff)/len(diff))

                except ZeroDivisionError:
                    Month_avg.append(0)
                    k=0

                diff.append(dr[date]-dw[date])
            
            
            

            
    city_diff=np.vstack((city_diff,Month_avg))
    #print(len(Month_avg))
    
city_diff=city_diff.T
#qp.insert(0, '0')

ght = pd.DataFrame(city_diff, columns=qp)
ght.insert(0, 'Month No.', [x+1 for x in range(102)])


# for i in range (len(qp)):
#     ght.loc[0,1+i]=qp[i]

#ght.drop(0, axis=1, inplace=True)

#fullname = os.path.join('/CleanResults/'+ file_name[0:-9], "/D_Margin_monthly(daywise)_" + file_name)
ght.to_csv("D_Margin_monthly(daywise)_" + file_name, index=False)




for i in qp:
    city_names.remove(i)
    
for i in qp:
    city_names2.remove(i)

for i in city_names:
	ghtW.drop(i, axis=1, inplace=True)

for i in city_names2:
	ghtR.drop(i, axis=1, inplace=True)
ghtR.drop('Month No.', axis=1, inplace=True)
ghtW.drop('Month No.', axis=1, inplace=True)

armW=ghtW.values
armR=ghtR.values
armR[armR == 0] = np.nan
armW[armW == 0] = np.nan


diff=armR-(armW/100)
diff[diff < 0] = 0

ghtD = pd.DataFrame(diff, columns=qp)
ghtD.insert(0, 'Month No.', [x+1 for x in range(102)])



ghtD.to_csv("M_Margin_monthly(monthwise)_"+ file_name, index=False)


