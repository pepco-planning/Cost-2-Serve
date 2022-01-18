import pandas as pd
import datetime
import os

targetValue_fileName = "0018_Picking_202205_November.csv"
targetValue_filePath = r"C:\Users\badamczyk\OneDrive - PEPCO\Desktop\Cost 2 Serve"
targetValue_filePathWithName = targetValue_filePath + "\\" + targetValue_fileName
targetValue_fileNamee = "0018_Loading_202105_November.csv"
targetValue_filePathh = r"C:\Users\badamczyk\OneDrive - PEPCO\Desktop\Cost 2 Serve"
targetValue = targetValue_filePathh + "\\" + targetValue_fileNamee

if os.path.isfile(targetValue_filePathWithName):
    os.remove(targetValue_filePathWithName)

resultTable = pd.DataFrame(columns=['OrderNo', 'PalletConfirmationDate', 'Pallet_ID','StoreNR','ArticleNoPLU','Quantity',
                                    'TCNo','DC_ID'])

resultTable.to_csv(targetValue_filePathWithName, mode="a+", index=False, header=True,sep=',')
l = list(os.listdir(r"C:\Users\badamczyk\OneDrive - PEPCO\Desktop\Cost 2 Serve"))
lista = []
for i in l:
    if i[0:30] == "0018_Pallet_confirmation202110" or i[0:30] == "0018_Pallet_confirmation202112" or i[0:30] == "0018_Pallet_confirmation202111" or i[0:30] == "0018_Pallet_confirmation202109" or i[0:30] == "0018_Pallet_confirmation202108" or i[0:30] == "0018_Pallet_confirmation202107":
        lista.append(i)

for i in lista:
    targetValue_fileName = i
    targetValue_filePath = r"C:\Users\badamczyk\OneDrive - PEPCO\Desktop\Cost 2 Serve"
    targetValue_filePathhWithNamee = targetValue_filePath + "\\" + targetValue_fileName
    if i[0:32] == "0018_Pallet_confirmation20210709" or i[0:32] == "0018_Pallet_confirmation20210716" or i[0:32] == "0018_Pallet_confirmation20210723" or i[0:32] == "0018_Pallet_confirmation20210730":
        df = pd.read_csv(targetValue_filePathhWithNamee, sep=',', low_memory=False, header=None , dtype = {'DC_ID': 'str','ArticleNoPLU':'str','StoreNR': 'str','Pallet_ID':'str'},
                     names = ['OrderNo', 'PalletConfirmationDate', 'Pallet_ID','StoreNR','ArticleNoPLU','Quantity','TCNo','DC_ID','x'])
        df.drop('x',axis =1,inplace=True)
        df = df[df.Quantity != 'Qty_in_TC']
        df[['OrderNo', 'PalletConfirmationDate', 'Pallet_ID','StoreNR','ArticleNoPLU','Quantity','TCNo','DC_ID']].to_csv(targetValue_filePathWithName, mode="a", index=False, header=False,sep=',')

    else:
        df = pd.read_csv(targetValue_filePathhWithNamee, sep=';', low_memory=False, header=None , dtype = {'DC_ID': 'str','ArticleNoPLU':'str','StoreNR': 'str','Pallet_ID':'str'},
                     names = ['OrderNo', 'PalletConfirmationDate', 'Pallet_ID','StoreNR','ArticleNoPLU','Quantity','TCNo','DC_ID'])
        df = df[df.Quantity != 'Qty_in_TC']
        df[['OrderNo', 'PalletConfirmationDate', 'Pallet_ID','StoreNR','ArticleNoPLU','Quantity','TCNo','DC_ID']].to_csv(targetValue_filePathWithName, mode="a", index=False, header=False,sep=',')

df = pd.read_csv(targetValue_filePathWithName, sep=',', low_memory=False,dtype = {'ArticleNoPLU':'str','DC_ID': 'str','StoreNR': 'str','Pallet_ID':'str'})
tablename = pd.read_csv(targetValue, sep=',', low_memory=False,dtype ={'Loading_Date':'str','PALLET_ID':'str','Store_NR':'str'})
tablename.drop('DC_ID',axis =1, inplace=True)
df['PalletConfirmationDate'] = pd.to_datetime(df['PalletConfirmationDate'])
df['PalletConfirmationDate'] = df['PalletConfirmationDate'].dt.date
df = df.merge(tablename, left_on = 'Pallet_ID', right_on='PALLET_ID', how = 'inner')
df = df.sort_values('PalletConfirmationDate')
df['Loading_Date'] = pd.to_datetime(df['Loading_Date'])
df['Loading_Date'] = df['Loading_Date'].dt.date
df = df[(df['Loading_Date']>=datetime.date(2021,11,1)) & (df['Loading_Date']<=datetime.date(2021,11,30))]
df.drop('Loading_Date', axis = 1, inplace=True)
df.drop('PALLET_ID',axis =1, inplace=True)
df.drop('Store_NR',axis =1, inplace=True)
df = df.dropna(axis=0)
df =df.drop_duplicates()

if os.path.exists(targetValue_filePathWithName):
    os.remove(targetValue_filePathWithName)

resultTable = pd.DataFrame(columns=['OrderNo', 'PalletConfirmationDate', 'Pallet_ID','StoreNR','ArticleNoPLU','Quantity',
                                    'TCNo','DC_ID'])
resultTable.to_csv(targetValue_filePathWithName, mode="a+", index=False, header=True,sep=',')
df[['OrderNo', 'PalletConfirmationDate', 'Pallet_ID','StoreNR','ArticleNoPLU','Quantity',
                                    'TCNo','DC_ID']].to_csv(targetValue_filePathWithName, mode="a", index=False, header=False,sep=',')
