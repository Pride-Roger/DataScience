import pandas as pd

V=pd.read_csv('For py_1.csv', header=0, sep=',')

pd.set_option('display.max_columns', None)

print(V.describe())