# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 21:56:57 2021

@author: ncuesuser
"""

import requests
import pandas as pd
#=================== Parameter Input File =====================================
web="http://202.90.198.41/index3.txt"  #web address of data provider
out="E:/BMKG/Data/"                                 # Directory of your output file

#=================== Computation ==============================================
r=requests.get(web)
data=r.text
data=data.splitlines()
header=data[2].split(sep='|')[1:]
for i in range(len(header)):
    header[i]=header[i].strip()
csv=pd.DataFrame(columns=header)
for i in range (4,len(data)-2):
    print(i)
    var=data[i].split(sep="|")[1:]
    df={header[0]:var[0],header[1]:var[1],header[2]:var[2],header[3]:var[3],
          header[4]:var[4],header[5]:var[5],header[6]:var[6],header[7]:var[7],
          header[8]:var[8],header[9]:var[9],header[10]:var[10],header[11]:var[11]}
    csv=csv.append(df,ignore_index=True)
idd=csv["Origin Time (GMT)"][0].strip().split()
idd=idd[0]
idd=idd.replace("-","_")
csv.to_csv(out+idd+".csv",index=False)