import pandas as pd
df1=pd.DataFrame({'key':['b','b','a','c','a','a','b'], 'data1': range(7)})
print(df1)
df2 =pd.DataFrame ({'key':['a','b','d'],'data2':range(3)})
print(df2)
merge_frame = pd.merge(df1,df2)
print(merge_frame)
merge_frame = pd.merge(df1,df2, on ='key')
print(merge_frame)
df3 = pd.DataFrame({'lkey': ['b', 'b', 'a', 'c', 'a', 'a', 'b'], 'data1': range(7)})
df4 = pd.DataFrame({'rkey': ['a', 'b', 'd'], 'data2': range(3)})
# And now we can merge as this
pd.merge(df3, df4, left_on='lkey', right_on='rkey')
pd.merge(df1, df2, how='outer')
df1 = pd.DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'b'], 'data1': range(6)})
df2 = pd.DataFrame({'key': ['a', 'b', 'a', 'b', 'd'], 'data2': range(5)})
pd.merge(df1, df2, on='key', how='left')
pd.merge(df1, df2, how='inner')
left = pd.DataFrame({'key1': ['foo', 'foo', 'bar'], 'key2': ['one', 'two', 'one'],
'lval': [1, 2, 3]})
print(left)
right = pd.DataFrame({'key1': ['foo', 'foo', 'bar', 'bar'], 'key2': ['one', 'one', 'one', 'two'],
'rval': [4, 5, 6, 7]})
print(right)
