import pandas as pd
import matplotlib.pyplot as pl

series = pd.Series(['A','B','C','D'],[10,20,30,40]) # second collection are the index
print(series)
print(series[10])
print(series.iloc[2])
series.name = "My_series"
print(series)
print(dict(series))
s1 = pd.Series([4,3,2,1],['a','b','c','d'])
s2 = pd.Series([4,2,5,1],['a','b','c','d'])
print(s1+s2)
print(s1.count())
print(s1.head(2))
print(s1.tail(2))
# 
mysquare = lambda x: x**2
print(s1.apply(mysquare))
print(s1.sort_index())
print(s1.sort_values())     # it returns the sorted serie, but don't apply the value to the serie
print(s1.sort_values(inplace=True))     # it returns nothing, but save the serie sorted

series = pd.Series([10,20,30,40],['A','B','C','D'])
series.name = "My_series"
# s1.plot
# s1.plot.bar()
series.plot.pie()
pl.show()

# series.to_sql()
series.to_csv('my_series.csv')

