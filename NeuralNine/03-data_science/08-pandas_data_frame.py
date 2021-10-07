import pandas as pd
import matplotlib.pyplot as pt

data = {
    'SSN': [123,512,612,751],
    'Name': ['ana','jesus','pepe','juan'],
    'Age': [18,23,54,19],
    'Weight': [65,67,78,70],
    'Gender': ['f','m','m','m'],
}
df = pd.DataFrame(data)
print(df)
df.set_index('SSN', inplace=True)
print(df)
# print(df.head(2))
print(df.tail(2))
# print(df.ndim)
# print(df.size)
# print(list(df.dtypes))
# print(df.shape)
# print(df.T)
print(df['Name'].iloc[1])
print(df.iloc[0])
# print(df.T.iloc[0])
print(df.describe())
df['Weight'].plot()
fig = pt.figure()
df.Age.plot.pie()

pt.show()

