import pandas as pd
import datetime
import os

targetValue_fileName = "0015_Loading_202205_November.csv"
targetValue_filePath = r"C:\Users\badamczyk\OneDrive - PEPCO\Desktop\Cost 2 Serve"
targetValue_filePathWithName = targetValue_filePath + "\\" + targetValue_fileName

if os.path.isfile(targetValue_filePathWithName):
    os.remove(targetValue_filePathWithName)
resultTable = pd.DataFrame(columns=['Loading_Date','PALLET_ID','Store_NR','rtcust'])
resultTable.to_csv(targetValue_filePathWithName, mode="a+", index=False, header=True,sep=',')
l = list(os.listdir(r"C:\Users\badamczyk\OneDrive - PEPCO\Desktop\Cost 2 Serve"))
lista = []
for i in l:
    if i[0:16] == "0015_Loadings_11":
        lista.append(i)


for i in lista:
    targetValue_fileName = i
    targetValue_filePath = r"C:\Users\badamczyk\OneDrive - PEPCO\Desktop\Cost 2 Serve"
    targetValue_filePathhWithNamee = targetValue_filePath + "\\" + targetValue_fileName
    parse_dates = ['Loading_Date']
    # separator dla 09 = ','
    # separator dla 10 = ';'
    # separator dla 11 = ','
    df = pd.read_csv(targetValue_filePathhWithNamee, sep=',', low_memory=False,skiprows = 1,parse_dates = parse_dates,dtype = {'Store_NR': 'str', 'PALLET_ID': 'str'},
                     header=None, names =['Loading_Date','PALLET_ID','Store_NR','rtcust'])

    df[['Loading_Date','PALLET_ID','Store_NR','rtcust']].to_csv(targetValue_filePathWithName, mode="a", index=False, header=False,sep=',')

parse_dates = ['Loading_Date']
df = pd.read_csv(targetValue_filePathWithName, sep=',', low_memory=False,dtype = {'PALLET_ID': 'str','Store_NR': 'str'},parse_dates = parse_dates)


df['Store_NR'] =df['Store_NR'].replace(['18'],'0018')
df['Store_NR'] =df['Store_NR'].replace(['6'],'0006')
df['Store_NR'] =df['Store_NR'].replace(['917'],'0917')
df['Store_NR'] =df['Store_NR'].replace(['968'],'0968')
df['Store_NR'] =df['Store_NR'].replace(['953'],'0953')
df['Store_NR'] =df['Store_NR'].replace(['869'],'0869')
df['Store_NR'] =df['Store_NR'].replace(['965'],'0965')
df['Store_NR'] =df['Store_NR'].replace(['959'],'0959')
df['Store_NR'] =df['Store_NR'].replace(['921'],'0921')
df['Store_NR'] =df['Store_NR'].replace(['919'],'0919')
df['Store_NR'] =df['Store_NR'].replace(['942'],'0942')
df['Store_NR'] =df['Store_NR'].replace(['994'],'0994')


df['Loading_Date'] = pd.to_datetime(df['Loading_Date'])
df['Loading_Date'] = df['Loading_Date'].dt.date
df = df.sort_values('Loading_Date')
df = df[(df['Loading_Date']>=datetime.date(2021,11,1)) & (df['Loading_Date']<=datetime.date(2021,11,30))]
df['DC_ID'] = '0015'
df.drop('rtcust',axis =1, inplace=True)
df =df.drop_duplicates()
df =df[df.Store_NR!= '0006']
df =df[df.Store_NR!= '0018']

if os.path.exists(targetValue_filePathWithName):
    os.remove(targetValue_filePathWithName)

resultTable = pd.DataFrame(columns=['Loading_Date','PALLET_ID','Store_NR','DC_ID'])
resultTable.to_csv(targetValue_filePathWithName, mode="a+", index=False, header=True,sep=',')
df[['Loading_Date','PALLET_ID','Store_NR','DC_ID']].to_csv(targetValue_filePathWithName, mode="a", index=False, header=False,sep=',')



##df.DC_ID.unique()
##len(df)
##len(df.PALLET_ID.unique())