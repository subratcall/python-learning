import pandas as pd
path = '/Users/macbook/Desktop/github-demo/US_Crime_Rates/US_Crime_Rates_1960_2014.csv'
df = pd.read_csv(path)

# inspect data
# print(df.head())

# print(df.info)

print(df.describe())

dic = {"hello": 1, "hi": 20}

for k, v in dic.items:
    print(k, v)
