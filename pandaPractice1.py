import pandas as pd
claims_df = pd.read_csv('/Users/satchidanandatripathy/Desktop/Study/PYTHON/Data/claims_priming.csv')

#Iterate data row by row

for index,data in claims_df.iterrows():
    print(index,data)

print('----------')
print('Print a particular column')
for index,data in claims_df.iterrows():
    print(data.patient_id)

