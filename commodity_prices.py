import pandas as pd

import analytical_info as ainfo
import generalFunc as gfunc

# Reading data
commodity_data = pd.read_csv(r'./commodity_prices.csv')
print('Top rows\n', commodity_data.head(5))     # getting top 5 rows of data
print('Infromation about each row\n', commodity_data.info())    # getting information about each each like null fields and data type containing in that row
print('Data Description\n', commodity_data.iloc[:, 1:].describe())  # getting some statical description of this data
print('Data Description including object fields\n', commodity_data.iloc[:,1:].describe(include='O').T)  # getting description of object field 
print('Unique values\n',commodity_data.nunique())    # getting number of unique values in each rows

# Getting information for data cleaning
print('Null values\n', commodity_data.isnull().sum().sum())
print('Duplicate values\n', commodity_data.duplicated().sum())
cleaned_data = commodity_data.iloc[:,1:]
print('Cleaned Data\n', cleaned_data.head(5))

# General analysis of given data
analytical_obj = ainfo.analysis(cleaned_data)
# print('Min value: ', analytical_obj.getMin(input('Enter field to find the minimum value: ')))    # getting minimum value any field
# print('Mean value: ', analytical_obj.getMean(input('Enter field mane for finding mean value: ')))    # getting mean of any field
# print('Max value: ', analytical_obj.getMax(input('Enter field name for finding max value: ')))    # getting maximum value of any field
# print(analytical_obj.getPrecentile(input('Enter field to find precentile: '), input('Enter precentile value: ')))    # getting precentile value of any field
# print('Skewness\n', analytical_obj.getSkewness(input('Enter field to find skewness: ')))    # getting skewness of any field

# complex analysis
print('Available analysis:\n1) Max value comparition\n')
analysis_type = input('Enter number of analysis you wanna preform: ')
match analysis_type:
    case '1':
        gfunc.maxValAnalysis(analyticalFunc=analytical_obj.getValueComparitionWithThreshold, data=cleaned_data)
    case _:
        raise ValueError('Invalid analysis type')