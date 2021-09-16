import pandas as pd
import re

cars_df = pd.read_csv('/Users/satchidanandatripathy/Desktop/Study/PYTHON/Data/mtcars2.csv')
print(cars_df.describe())

print('create a new columns by applying sum')
cars_df['Total']=cars_df.iloc[:,3:5].sum(axis=1)
#This will add the values of 4th i.e. cyl and 5th i.d. disp columns in to the Total column
#axis = 1 represent horizontal addition
print(cars_df.head(5))

new_df=list(cars_df.columns.values)
#add 2nd 3rd and last column to total values
new_df['Total_values']=new_df[3:5]+[new_df[-1]]
print(new_df)

