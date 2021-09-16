import pandas as pd
from openpyxl.workbook import Workbook
claims_df = pd.read_csv('/Users/satchidanandatripathy/Desktop/Study/PYTHON/Data/claims_priming.csv')
print('Few stastical data about the dataframe')
print(claims_df.describe())

print('Sort data in the dataframe by descending order of amount and print top 3 rows')
sorted_df=claims_df.sort_values('total_cost',ascending=False).head(4)
print(sorted_df[['patient_id','provider_id','total_cost']])

print('drop columns from data frame ')

sorted_df=sorted_df.drop(columns=['patient_id'])
print(sorted_df)

####### DATA FILTERING
##Filter data where total_cost not equal to 0 and claim_id =CF#1012078NN or 1=2

df=claims_df.loc((['claim_id']=='CF#1012078NN') & (['total_cost']!=0)|(1==2) )
print(df)

df1=claims_df.loc[(claims_df['claim_id']=='CF#1012078NN') ]

print(df1)


# FILTER ALL THE CLAIMS WHERE THE PROVIDER_ID CONTAINS 3T

print(claims_df.loc[claims_df['provider_id'].str.contains('3T')])
print('---------------')
print('Add one derived column')
sorted_df['Total']=sorted_df['total_cost']*5
print(sorted_df)


print('save data into another csv ')
sorted_df.to_csv('/Users/satchidanandatripathy/Desktop/Study/PYTHON/Data/new.csv')
#for excel we can do to_excel() index=False means it will not place the default first (index) col
# To save in excel we need to from openpyxl.workbook import Workbook
sorted_df.to_excel('/Users/satchidanandatripathy/Desktop/Study/PYTHON/Data/new1.xlsx',index=False)
