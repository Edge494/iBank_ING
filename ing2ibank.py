__author__ = 'Edmond van der Plas'
__date__ = '16-11-2013'
__version__ = '0.2.1'

import pandas as pd

import sys

#Importeren van de csv data waarbij de filename van het csv bestand ingegeven is als argument in het starten van het python script
df = pd.read_csv(sys.argv[1], usecols=[0,1,3,5,6,8])

#Hernoemen van 2 kolommen voor makkelijker gebruik
df.rename(columns={'Af Bij': 'afbij'}, inplace=True)
df.rename(columns={'Bedrag (EUR)': 'Bedrag'}, inplace=True)
df.rename(columns={'Naam / Omschrijving': 'Omschrijving'}, inplace=True)

#Als scheidingsteken voor decimalen een punt instellen ipv een comma en daarna een float maken van de bedragen (als type)
for i in range (0, len(df)):
    df.ix[i,'Bedrag'] = df.ix[i,'Bedrag'].replace( '.', '')
    df.ix[i,'Bedrag'] = df.ix[i,'Bedrag'].replace( ',', '.')
df['Bedrag'] =  df['Bedrag'].astype(float)

#Berekening maken of bedrag positief of negatief is
df['Bedrag2'] = df.apply(lambda row: (row['Bedrag']
                                             if row['afbij']=='Bij'
                                            else -row['Bedrag']), axis=1)

#Kolommen selecteren voor output
df2 = df[['Datum','Omschrijving', 'Bedrag2','Tegenrekening','Mededelingen']]

#Datastructuur naar csv schrijven
df2.to_csv('test_result.csv', sep=',', na_rep='0', dtype=int)


