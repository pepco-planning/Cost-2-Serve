import pandas as pd
import datetime
import os

targetValue_fileName = "0015_Picking_202205_November.csv"
targetValue_filePath = r"C:\Users\badamczyk\OneDrive - PEPCO\Desktop\Cost 2 Serve"
targetValue_filePathWithName = targetValue_filePath + "\\" + targetValue_fileName
targetValue_fileNamee = "0015_Loading_202205_November.csv"
targetValue_filePathh = r"C:\Users\badamczyk\OneDrive - PEPCO\Desktop\Cost 2 Serve"
targetValue = targetValue_filePathh + "\\" + targetValue_fileNamee

if os.path.isfile(targetValue_filePathWithName):
    os.remove(targetValue_filePathWithName)
resultTable = pd.DataFrame(columns=['OrderNo','PalletConfirmationDate','Pallet_ID','StoreNR','ArticleNoPLU','Quantity','TCNo','DC_ID'])
resultTable.to_csv(targetValue_filePathWithName, mode="a+", index=False, header=True,sep=',')
l = list(os.listdir(r"C:\Users\badamczyk\OneDrive - PEPCO\Desktop\Cost 2 Serve"))
lista = []
for i in l:
    if i[0:23] == "0015_pallet_conf_202110" or i[0:23] == "0015_pallet_conf_202109" or i[0:23] == "0015_pallet_conf_202111" or i[0:23] == "0015_pallet_conf_202108" or i[0:23] == "0015_pallet_conf_202107":
        lista.append(i)

for i in lista:
    targetValue_fileName = i
    targetValue_filePath = r"C:\Users\badamczyk\OneDrive - PEPCO\Desktop\Cost 2 Serve"
    targetValue_filePathhWithNamee = targetValue_filePath + "\\" + targetValue_fileName
    if i[0:23] == "0015_pallet_conf_202107":
        df = pd.read_csv(targetValue_filePathhWithNamee, sep=';', low_memory=False, header=None ,dtype = {'StoreNR':'str','ArticleNoPLU':'str','DC_ID':'str', 'Pallet_ID':'str'}, 
                     names =['OrderNo','PalletConfirmationDate','Pallet_ID','StoreNR','ArticleNoPLU','Quantity','TCNo','DC_ID'])
        df = df[df.Quantity != 'quantity']
        df[['OrderNo','PalletConfirmationDate','Pallet_ID','StoreNR','ArticleNoPLU','Quantity','TCNo','DC_ID']].to_csv(targetValue_filePathWithName, mode="a", index=False, header=False,sep=',')
    else:
        df = pd.read_csv(targetValue_filePathhWithNamee, sep=',', low_memory=False, header=None ,dtype = {'StoreNR':'str','ArticleNoPLU':'str','DC_ID':'str', 'Pallet_ID':'str'}, 
                     names =['OrderNo','PalletConfirmationDate','Pallet_ID','StoreNR','ArticleNoPLU','Quantity','TCNo','stcust','DC_ID'])
        df.drop('stcust',axis =1, inplace=True)
        df = df[df.Quantity != 'quantity']
        df[['OrderNo','PalletConfirmationDate','Pallet_ID','StoreNR','ArticleNoPLU','Quantity','TCNo','DC_ID']].to_csv(targetValue_filePathWithName, mode="a", index=False, header=False,sep=',')

df = pd.read_csv(targetValue_filePathWithName, sep=',', low_memory=False,
                 dtype = {'StoreNR':'str','ArticleNoPLU':'str','DC_ID':'str','Pallet_ID':'str'})

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
df =df.drop_duplicates()
df = df.dropna(axis=0)

if os.path.exists(targetValue_filePathWithName):
    os.remove(targetValue_filePathWithName)

resultTable = pd.DataFrame(columns=['OrderNo','PalletConfirmationDate','Pallet_ID','StoreNR','ArticleNoPLU','Quantity','TCNo','DC_ID'])
resultTable.to_csv(targetValue_filePathWithName, mode="a+", index=False, header=True,sep=',')
df[['OrderNo','PalletConfirmationDate','Pallet_ID','StoreNR','ArticleNoPLU','Quantity','TCNo','DC_ID']].to_csv(targetValue_filePathWithName, mode="a", index=False, header=False,sep=',')


##df.info()
##len(df.Pallet_ID.unique())
##print(df.PalletConfirmationDate.unique())

