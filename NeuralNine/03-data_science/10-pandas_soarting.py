import pandas as pd
import numpy as np

data = {
    'SSN': [123,512,612,751],
    'Name': ['ana','jesus','pepe','juan'],
    'Age': [18,23,54,18],
    'Weight': [65,65,78,70],
    'Gender': ['f','m','m','m'],
}

df = pd.DataFrame(data)
df.set_index('SSN', inplace=True)
print(df['Weight'].apply(np.sin))
print(df['Weight'].apply(lambda x: x * 100))

for key, value in df['Age'].iteritems():
    print(f"{key}: {value}")

df.sort_index(inplace=True)
print(df)
df.sort_values(by=['Age', 'Weight'], inplace=True)
print(df)
