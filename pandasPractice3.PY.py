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
#new_df['Total_values']=new_df[3:5]+[new_df[-1]]
#print(new_df)

# Drop a column
#new_df = new_df.drop(columns=['Total'])

#Conditional
#cars_df.loc[(df['Total']=='Value1')|(df['Total']=='Value2')] filter data when a or b mathches

#similary you can use when a ='value 1' and b>xyz etc etc


#from cars_df perform below Aggregate functions
print('Columns in the data frame are ',end='')
print(cars_df.columns)

#Get sum of the column Total

print('The sum of total is ')
print(cars_df['Total'].sum(axis=0))

print('Average of the columns group by gear and sort them')
print(cars_df.groupby(['gear']).mean().sort_values('Total',ascending=False))

print('count of the columns group by gear')
print(cars_df.groupby(['gear']).count())
