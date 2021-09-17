import pandas as pd
claims_df = pd.read_csv('/Users/satchidanandatripathy/Desktop/Study/PYTHON/Data/claims_priming.csv')

#Iterate data row by row


print('----------')
print('Print a particular column')
print('patient_id')
for index,data in claims_df.iterrows():
    print(data.patient_id)

print('---------------------------------------')

    #also we can do like it will fetch only 5 rows into df

for df in pd.read_csv('/Users/satchidanandatripathy/Desktop/Study/PYTHON/Data/claims_priming.csv',chunksize=5):
    print(df)
##################


print('---------------------------------------')

print('-----ALL COLUMNS ------')
print('')
for index,data in claims_df.iterrows():
    print(index,data)

