import numpy as np 
import pandas as pd 

data_raw = pd.read_csv("https://raw.githubusercontent.com/SebastianS09/Malaria/master/Data/Malaria.csv")

print(data_raw.head(10))

###Data cleaning 

####Removing unecessary geographical precision and study information
data_raw.columns = [c.replace(' ', '_') for c in data_raw.columns]
col_rm = ['GAUL_Admin2','Full_Name','LatLong_Source','Source_Title']
data_rm = data_raw.drop(col_rm, axis=1)

print(data_rm.head(10))

#### Replacing Y and NaN with 0 and 1 for ease of understanding (col 7 to 33)

data_clean = data_rm.copy()

aneo = list(data_clean)[6:32]
data_clean[aneo] = data_clean[aneo].replace(['Y'],1)
data_clean[aneo] = data_clean[aneo].fillna(0)

print(data_clean.head(10))

####Check if other species are relevant 

other_f = data_clean['Other_Anopheline_species'].str.split(', ', expand=True)
other_f.fillna(0,inplace=True)

a = other_f[0].value_counts().to_frame()
for i in list(other_f.drop(0,axis=1)):
    a = a.join(other_f[i].value_counts().to_frame())
a.fillna(0,inplace=True)

a.sum(axis=1).sort_values(ascending = False)
data_clean[aneo].sum(axis=0).sort_values(ascending = False)

