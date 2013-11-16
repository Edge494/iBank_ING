__author__ = 'Edmond van der Plas'
__date__ = '16-11-2013'
__version__ = '0,1'


import pandas as pd

#Importeren van de csv data
df = pd.read_csv("test.csv", usecols=[0,3,5,6,8])

#Hernoemen van 2 kolommen voor makkelijker gebruik
df.rename(columns={'Af Bij': 'afbij'}, inplace=True)
df.rename(columns={'Bedrag (EUR)': 'Bedrag'}, inplace=True)

#Als scheidingsteken voor decimalen een punt instellen ipv een comma en daarna een float maken van de bedragen (als type)
for i in range (0, len(df)):
    df.ix[i,'Bedrag'] = df.ix[i,'Bedrag'].replace( '.', '')
    df.ix[i,'Bedrag'] = df.ix[i,'Bedrag'].replace( ',', '.')
df['Bedrag'] =  df['Bedrag'].astype(float)

#Nodig voor berekening hieronder
df['C'] = df.afbij.apply(
               lambda x: (1 if x == 'Bij' else 1))

#Berekening maken of bedrag positief of negatief is
df['Bedrag2'] = df.apply(lambda row: (row['Bedrag']*row['C']
                                             if row['afbij']=='Bij'
                                            else -row['Bedrag']*row['C']), axis=1)

#Kolommen selecteren voor output
df2 = df[['Datum','Mededelingen', 'Bedrag2','Tegenrekening']]

#Datastructuur naar csv schrijven
df2.to_csv('test_result.csv', sep=',', na_rep='0', dtype=int)


