import pandas as pd
claims_df = pd.read_csv('/Users/satchidanandatripathy/Desktop/Study/PYTHON/Data/claims_priming.csv')

#pd.read_excel('abc.xlsx')  To read data from excel
#pd.read_csv('abc.txt',delimiter='\t')
print('First 5 records')
print(claims_df.head(5))

print('Last 5 records')
print(claims_df.tail(5))

print('Columns in the data frame')
print(claims_df.columns)

print('First 5 records of A particular column')
print(claims_df['claim_id'].head(5))
# Another way to access
print('-----')
print(claims_df.patient_id[0:5])

print('First 10 patient_id and claim_id')
print(claims_df[['patient_id','claim_id']].head(10))

####### The iloc function
print('Value of first row')
print(claims_df.iloc[0])
print('Value of first 3 rows')
print(claims_df.iloc[0:2])
#iloc to fetch data as matrix format
print('Value of second  row and 3rd column')
print(claims_df.iloc[1,2])

print('Value of first and second  row and first second and 3rd column')
print(claims_df.iloc[0:2,0:3])

print('Value of first and second  row and All columns')
print(claims_df.iloc[0:2,:])

######## the loc function
print('select data from the dataframe where prover id N3T7500A ')
claims_df.loc[claims_df['provider_id']=="N3T7500A"]


