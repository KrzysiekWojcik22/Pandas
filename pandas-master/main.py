import pandas as pd
df = pd.read_csv('pokemon_data.csv')
#df_xls = pd.read_excel('pokemon_data.xlsx')
#df_txt = pd.read_csv('pokemon_data.txt', delimiter='\t')
#print(df[['Name', 'Type 1', 'HP']][0:15])
#print(df.iloc[0:4])
#print(df.iloc[2,1])
'''
for index, row in df.iterrows():
    print(index,row['Name'])
    
'''
#print(df.loc[df['Type 1'] == "Water"])
#print(df.describe())
#print(df.sort_values(['Type 1','HP'], ascending=True))
#print(df.head(5))
#df['Total']=df['HP']+df['Defense']+df['Sp. Atk']+df['Sp. Def']+df['Speed']


print(df.head(5))