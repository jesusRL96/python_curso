import pandas as pd 
 
names = {
'SSN': [8,3,5,6],
'Name': ['Anna','Jesus','jose','pepe']
}
ages = {
'SSN': [1,3,8,4],
'Age': [23,22,15,40]
}

df1 = pd.DataFrame(names)
df2 = pd.DataFrame(ages)

df = pd.merge(df1,df2,on='SSN', how='right')
df.set_index('SSN', inplace=True)
df.sort_index(inplace=True)
print(df)