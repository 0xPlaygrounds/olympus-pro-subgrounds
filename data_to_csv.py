from data_fetcher import *

df = fetch_bonds_since(0)
df.to_csv('bonds.csv')