import pandas as pd
import datetime
import os

targetValue_fileName = "0006_Loading_202205_November.csv"
targetValue_filePath = r"C:\Users\badamczyk\OneDrive - PEPCO\Desktop\Cost 2 Serve"
targetValue_filePathWithName = targetValue_filePath + "\\" + targetValue_fileName

if os.path.isfile(targetValue_filePathWithName):
    os.remove(targetValue_filePathWithName)

resultTable = pd.DataFrame(columns=['LOADING_DATA', 'PALLET_ID', 'STORE_NR'])
resultTable.to_csv(targetValue_filePathWithName, mode="a+", index=False, header=True,sep=',')
l = list(os.listdir(r"C:\Users\badamczyk\OneDrive - PEPCO\Desktop\Cost 2 Serve"))
lista = []
for i in l:
    if i[0:21] == "0006_LD_PALLET_202111" or i[0:21] == "0006_LD_PALLET_202112" or i[0:21] == "0006_LD_PALLET_202110":
        lista.append(i)

for i in lista:
    targetValue_fileName = i
    targetValue_filePath = r"C:\Users\badamczyk\OneDrive - PEPCO\Desktop\Cost 2 Serve"
    targetValue_filePathhWithNamee = targetValue_filePath + "\\" + targetValue_fileName
    df = pd.read_csv(targetValue_filePathhWithNamee, sep=';', low_memory=False, dtype ={'LOADING_DATA':'str','PALLET_ID':'str','STORE_NR':'str'})
    df[['LOADING_DATA', 'PALLET_ID', 'STORE_NR']].to_csv(targetValue_filePathWithName, mode="a", index=False, header=False,sep=',')


df = pd.read_csv(targetValue_filePathWithName, sep=',', low_memory=False,dtype ={'LOADING_DATA':'str','PALLET_ID':'str','STORE_NR':'str'})
df = df[df.STORE_NR != 'PEPCO']
df =df.drop_duplicates()

### Usuwanie danych dla października oraz listopada
usun = ['000000000004967749','000000000004967750','000000000004967759','000000000004967760','000000000004967761',
        '000000000004967762','000000000004967763','000000000004967765','000000000004967766','000000000004967767','000000000004967768']
for i in usun:
    df = df[df.PALLET_ID != i]


df = df.sort_values('LOADING_DATA')
df['LOADING_DATA'] = pd.to_datetime(df['LOADING_DATA'])
df['LOADING_DATA'] = df['LOADING_DATA'].dt.date
df = df[(df['LOADING_DATA']>=datetime.date(2021,11,1)) & (df['LOADING_DATA']<=datetime.date(2021,11,30))]


if os.path.exists(targetValue_filePathWithName):
    os.remove(targetValue_filePathWithName)

resultTable = pd.DataFrame(columns=['LOADING_DATA', 'PALLET_ID', 'STORE_NR'])
resultTable.to_csv(targetValue_filePathWithName, mode="a+", index=False, header=True,sep=',')

df[['LOADING_DATA', 'PALLET_ID', 'STORE_NR']].to_csv(targetValue_filePathWithName, mode="a", index=False, header=False,sep=',')

# zapytania do sprawdzania tabel i ich zawartości
#len(df.PALLET_ID.unique())
#len(df)
#df.LOADING_DATA.unique()

