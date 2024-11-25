import pandas as pd

df = pd.read_csv("paraules_temàtica_penjat.csv")

for x in range(len(df)):
    paraula = df['WORD'][x]
    tematica = df['THEME'][x]
    
    