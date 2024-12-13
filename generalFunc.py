import visual_analysis as vana

def maxValAnalysis(data, analyticalFunc):
    col1 = input('Enter col1: ')
    col2 = input('Enter col2: ')
    print('Max value comparition between columns\n ', analyticalFunc(input('Enter operator: '), float(input("Enter threshold: ")), col1, col2))    # getting max value comparition between two column
    print('Bar graph for comparitive analysis\n')
    vana.visuals.histo(dataSet=abs(data[col1].values - data[col2].values), label=input('Enter label of x axis: '))    # showing a histogram with all the difference in the value of two columns

