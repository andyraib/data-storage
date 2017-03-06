import pandas as pd
import json

with open ('/home/administradorcito/data-graduates/Introduction_01/data/countries.json') as data_file:
	data = json.load(data_file)

keys = data[0].keys()
df = pd.DataFrame(columns = keys)

print(df)

for i in data:
	for key, value in i:
		print(value)
