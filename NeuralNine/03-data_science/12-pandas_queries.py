import pandas as pd 

df = pd.read_csv('./03-data_science/people.csv', delimiter=',')
df.set_index('SSN', inplace=True)
print(df)

print(df.loc[(df['Age'] >= 23) & (df['Height'] >= 165)]['Name'])