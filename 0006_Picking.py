


import pandas as pd
import datetime
import os

targetValue_fileName = "0006_Picking_202205_November.csv"
targetValue_filePath = r"C:\Users\badamczyk\OneDrive - PEPCO\Desktop\Cost 2 Serve"
targetValue_filePathWithName = targetValue_filePath + "\\" + targetValue_fileName
targetValue_fileNamee = "0006_Loading_202205_November.csv"
targetValue_filePathh = r"C:\Users\badamczyk\OneDrive - PEPCO\Desktop\Cost 2 Serve"
targetValue = targetValue_filePathh + "\\" + targetValue_fileNamee


if os.path.isfile(targetValue_filePathWithName):
    os.remove(targetValue_filePathWithName)
resultTable = pd.DataFrame(columns=['OrderNo','PalletConfirmationDate','Pallet_ID','StoreNR', 'ArticleNoPLU','Quantity', 'TCNo', 'DC_ID'])
resultTable.to_csv(targetValue_filePathWithName, mode="a+", index=False, header=True,sep=',')


l = list(os.listdir(r"C:\Users\badamczyk\OneDrive - PEPCO\Desktop\Cost 2 Serve"))
lista = []
for i in l:
    if i[0:16] == "0006_PICK_202109" or i[0:16] == "0006_PICK_202110" or i[0:16] == "0006_PICK_202111" or i[0:16] == "0006_PICK_202112" :
        lista.append(i)


for i in lista:
    targetValue_fileName = i
    targetValue_filePath = r"C:\Users\badamczyk\OneDrive - PEPCO\Desktop\Cost 2 Serve"
    targetValue_filePathhWithNamee = targetValue_filePath + "\\" + targetValue_fileName

    df = pd.read_csv(targetValue_filePathhWithNamee,
                      sep=';', skiprows=1, header=None, dtype = {'Pallet_ID': 'str','DC_ID':'str','StoreNR':'str'},
                     names=['OrderNo', 'PalletConfirmationDate', 'Pallet_ID', 'StoreNR', 'ArticleNoPLU', 'Quantity','TCNo', 'DC_ID'], low_memory=False)
    df[['OrderNo','PalletConfirmationDate','Pallet_ID','StoreNR', 'ArticleNoPLU','Quantity', 'TCNo', 'DC_ID']].to_csv(targetValue_filePathWithName, mode="a", index=False, header=False,sep=',')


df = pd.read_csv(targetValue_filePathWithName, sep=',', low_memory=False,dtype = {'Pallet_ID': 'str','DC_ID':'str','StoreNR':'str'})
tablename = pd.read_csv(targetValue, sep=',', low_memory=False,dtype ={'LOADING_DATA':'str','PALLET_ID':'str','STORE_NR':'str'})
df = df.dropna(axis=0)
df = df.sort_values('PalletConfirmationDate')
df['PalletConfirmationDate'] = pd.to_datetime(df['PalletConfirmationDate'])
df['PalletConfirmationDate'] = df['PalletConfirmationDate'].dt.date

df = df.merge(tablename, left_on = 'Pallet_ID', right_on='PALLET_ID', how = 'inner')

df['LOADING_DATA'] = pd.to_datetime(df['LOADING_DATA'])
df['LOADING_DATA'] = df['LOADING_DATA'].dt.date
df = df[(df['LOADING_DATA']>=datetime.date(2021,11,1)) & (df['LOADING_DATA']<=datetime.date(2021,11,30))]


df.drop('LOADING_DATA', axis = 1, inplace=True)
df.drop('PALLET_ID',axis =1, inplace=True)
df.drop('STORE_NR',axis =1, inplace=True)
df =df.drop_duplicates()
df = df.dropna(axis=0)


if os.path.exists(targetValue_filePathWithName):
    os.remove(targetValue_filePathWithName)

resultTable = pd.DataFrame(columns=['OrderNo','PalletConfirmationDate','Pallet_ID','StoreNR', 'ArticleNoPLU','Quantity', 'TCNo', 'DC_ID'])
resultTable.to_csv(targetValue_filePathWithName, mode="a+", index=False, header=True,sep=',')
df[['OrderNo','PalletConfirmationDate','Pallet_ID','StoreNR', 'ArticleNoPLU','Quantity', 'TCNo', 'DC_ID']].to_csv(targetValue_filePathWithName, mode="a", index=False, header=False,sep=',')


#len(df.Pallet_ID.unique())
#df.OrderNo.unique()