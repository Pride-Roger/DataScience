import pandas as pd

V={'Col_1': [1,2,3,4], 'Col_2': [5,6,7,8],
   'Cols_3': [9,10,11,12]}

DF=pd.DataFrame(data=V)

Count_Rows=DF.shape[0]

Count_cols=DF.shape[1]

print(DF)

print('No. of rows present:',Count_Rows)

print('No. of cols present:',Count_cols)