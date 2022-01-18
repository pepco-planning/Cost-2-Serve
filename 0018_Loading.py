import pandas as pd
import datetime
import numpy
import os

targetValue_fileName = "0018_Loading_202105_November.csv"
targetValue_filePath = r"C:\Users\badamczyk\OneDrive - PEPCO\Desktop\Cost 2 Serve"
targetValue_filePathWithName = targetValue_filePath + "\\" + targetValue_fileName

if os.path.isfile(targetValue_filePathWithName):
    os.remove(targetValue_filePathWithName)

resultTable = pd.DataFrame(columns=['Loading_Date', 'PALLET_ID', 'Store_NR','DC_ID'])
resultTable.to_csv(targetValue_filePathWithName, mode="a+", index=False, header=True,sep=',')

l = list(os.listdir(r"C:\Users\badamczyk\OneDrive - PEPCO\Desktop\Cost 2 Serve"))
lista = []
for i in l:
    if i[0:18] == "0018_Loading202111" or i[0:18] == "0018_Loading202112" or i[0:18] == "0018_Loading202110":
        lista.append(i)

for i in lista:
    targetValue_fileName = i
    targetValue_filePath = r"C:\Users\badamczyk\OneDrive - PEPCO\Desktop\Cost 2 Serve"
    targetValue_filePathhWithNamee = targetValue_filePath + "\\" + targetValue_fileName
    df = pd.read_csv(targetValue_filePathhWithNamee,  sep=';',dtype = {'Store_NR': 'str', 'DC_ID':'str','PALLET_ID':'str'}, skiprows= 1, header=None, 
                     names=['Loading_Date','PALLET_ID','Store_NR','DC_ID'], low_memory=False)
    df['DC_ID'] = '0018'
    df[['Loading_Date', 'PALLET_ID', 'Store_NR','DC_ID']].to_csv(targetValue_filePathWithName, mode="a", index=False, header=False,sep=',')

df = pd.read_csv(targetValue_filePathWithName, sep=',', low_memory=False,dtype = {'Store_NR': 'str', 'DC_ID':'str','PALLET_ID':'str'})
df['Loading_Date'] = pd.to_datetime(df['Loading_Date'])
df['Loading_Date'] = df['Loading_Date'].dt.date
df =df.drop_duplicates()

# palety sie nie zgadzaly, musialy zostac usuniete
usun = ['GS0000694476',
'GS0000694479',
'GS0000703165',
'GS0000704495',
'GS0000708803',
'GS0000717319',
'GS0000717320',
'GS0000719135',
'GS0000720939',
'GS0000722161',
'GS0000724375',
'GS0000724781',
'GS0000726240',
'GS0000727233',
'GS0000727236',
'GS0000727264',
'GS0000727513',
'GS0000727547',
'GS0000727859',
'GS0000727867',
'GS0000728680',
'GS0000729134',
'GS0000729135',
'GS0000729137',
'GS0000729150',
'GS0000729166',
'GS0000729174',
'GS0000729732',
'GS0000730053',
'GS0000730531',
'GS0000731137',
'GS0000731687',
'GS0000731860',
'GS0000736176',
'GS0000756828',
'GS0000757510',
'GS0000761707',
'GS0000763987',
'GS0000766513',
'GS0000768460',
'GS0000768485',
'GS0000768628',
'GS0000768906',
'GS0000768986',
'GS0000768993',
'GS0000768998',
'GS0000769654',
'GS0000769656',
'GS0000769658',
'GS0000771499',
'GS0000771807',
'GS0000771813',
'GS0000771828',
'GS0000771843',
'GS0000771852',
'GS0000771879',
'GS0000771887',
'GS0000772074',
'GS0000773159',
'GS0000773777']
for i in usun:
    df = df[df.PALLET_ID != i]

df = df.sort_values('Loading_Date')
df = df[(df['Loading_Date']>=datetime.date(2021,11,1)) & (df['Loading_Date']<=datetime.date(2021,11,30))]

if os.path.exists(targetValue_filePathWithName):
    os.remove(targetValue_filePathWithName)

resultTable = pd.DataFrame(columns=['Loading_Date','PALLET_ID','Store_NR','DC_ID'])
resultTable.to_csv(targetValue_filePathWithName, mode="a+", index=False, header=True,sep=',')
df[['Loading_Date','PALLET_ID','Store_NR','DC_ID']].to_csv(targetValue_filePathWithName, mode="a", index=False, header=False,sep=',')

df.Loading_Date.unique()

# kod do wyciagania palet ktore ukazują sie dwu krotnie
#k = df.PALLET_ID
#d = {'col1': k}
#dff = pd.DataFrame(data=d)
#dff.head()
#df.groupby('PALLET_ID').nunique()['Loading_Date']
#df2 = df.groupby('PALLET_ID').nunique()
#df2[df2['Loading_Date']==2]