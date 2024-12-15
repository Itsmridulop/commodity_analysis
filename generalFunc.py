import visual_analysis as vana
import pandas as pd

def maxValAnalysis(data, analyticalFunc):
    col1 = input('Enter col1: ')
    col2 = input('Enter col2: ')
    print('Max value comparition between columns\n ', analyticalFunc(input('Enter operator: '), float(input("Enter threshold: ")), col1, col2))    # getting max value comparition between two column
    print('Bar graph for comparitive analysis\n')
    vana.visuals.histo(dataSet=abs(data[col1].values - data[col2].values), label=input('Enter label of x axis: '))    # showing a histogram with all the difference in the value of two columns

def priceTrend(data):
    melted_data = pd.melt(data, id_vars=['date'], var_name='commodity', value_name='price') # melting the data to get the stock and price
    vana.visuals.line(x='date', y='price', hue='commodity', rotation=45, data=melted_data) # showing the line graph of the stock price

def priceFluctuation(data):
    commodity_price = data.drop(columns='date').std()
    print(f'The commodity with the highest fluctuation: {commodity_price.idxmax()} with price {commodity_price.max()}')
    vana.visuals.bar(xVal='index', yVal=0,dataSet=commodity_price.reset_index(), rotation=45) # showing the bar graph of the fluctuation of the stock price