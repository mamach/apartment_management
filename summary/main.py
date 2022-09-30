from cmath import isnan, nan
import pandas as pd
import pdb
import re

CATEGORY_TYPE='OUT'

trim = re.compile(r'[^\d.,]+')

def drawline():
    print('')
    print('----------------------------------------------')
    print('')
    

##
# 1. READING INPUT FILE
##
input_filepath = './input.xlsx'
# input_filepath = './input.csv'

##
# 2. READING FILE WITH PANDAS
##
xl_file = pd.ExcelFile(input_filepath)
# dfs = {sheet_name: xl_file.parse(sheet_name) for sheet_name in xl_file.sheet_names}
df =pd.read_excel(input_filepath, sheet_name='in')
# df = pd.read_csv(input_filepath)

##
# 3. Sort by Category
##
df = df.sort_values('Category')

##
# 4. Identify Categories
##
categories = df['Category'].unique()
print(categories)

##
# 5. Calculate sum by each category
##
for category in categories:
    if isinstance(category, str):
        # print( "processing category : " + category)
        category_itemwise_values = df.loc[df['Category']==category, CATEGORY_TYPE].to_dict()
        itemwise_sum = 0
        for index in category_itemwise_values:
            # print(type(category_itemwise_values[index]))
            mystring = category_itemwise_values[index]
            result = trim.sub('', mystring)
            # print(type(int(result)))
            itemwise_sum += float(result)
            # print (category_itemwise_values[index])
        # pdb.set_trace()
        print(str(category) + " : " + str(itemwise_sum))


##
# 6. Save Result
##

# drawline()
# print(df.shape)
# drawline()
# print(df.columns)
# drawline()
# print(df.info())
# drawline()
# print(df.head(3))
# drawline()
# print(df['key'].head(3))
drawline()
# print(df.sort_values('Category'))

# print(category_itemwise_values)

# df.query['Category'=='MAINTAINANCE RECEIVED']
