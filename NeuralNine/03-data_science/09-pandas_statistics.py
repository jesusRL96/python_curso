import pandas as pd
import matplotlib.pyplot as pt

data = {
    'SSN': [123,512,612,751],
    'Name': ['ana','jesus','pepe','juan'],
    'Age': [18,23,54,19],
    'Weight': [65,65,78,70],
    'Gender': ['f','m','m','m'],
}

df = pd.DataFrame(data)
df.set_index('SSN', inplace=True)
# print(df['Age'].count())
print(df.count())
# print(df['Age'].sum())
print(df.sum())
print(df.prod())
print(df['Weight'].mode())  # mode
print(df['Weight'].median())  # median
print(df['Weight'].mean())  # average
print(df['Weight'].std())  # standard diviation

print(df.describe())

