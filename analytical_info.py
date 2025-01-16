import visual_analysis as vana

class analysis:
    def __init__(self, dataSet: object):
        self.dataSet = dataSet

    # Protected functions
    def _calcPrecentile(self, dataCol: str, prec: str) -> str:
        return self.dataSet[dataCol].describe()[prec+'%']

    # public functions
    def getMean(self, dataCol: str) -> str:
        return self.dataSet[dataCol].mean()

    def  getMax(self, dataCol: str) -> str:
        return self.dataSet[dataCol].max()
    
    def getMin(self, dataCol: str) -> str:
        return self.dataSet[dataCol].min()
    
    def getPrecentile(self, dataCol: str, prec: str):
        match prec:
            case '75':
                print(f'75 precentile value of field {dataCol}: ', self._calcPrecentile(dataCol,prec))
            case '50':
                print(f'50 precentile value of field {dataCol}: ', self._calcPrecentile(dataCol,prec))
            case '25':
                print(f'25 precentile value of field {dataCol}: ', self._calcPrecentile(dataCol,prec))
            case _:
                raise ValueError('Precentile value must only be 25, 50 or 75')
    
    def getSkewness(self, dataCol: str) -> object:
        return self.dataSet[dataCol].skew()
    
    def getValueComparitionWithThreshold(self,opt:str, threshold: float | None, dataCol1: str, dataCol2: str) -> object:
        match opt:
            case '<':
                return self.dataSet[self.dataSet[dataCol1]-self.dataSet[dataCol2] < threshold][[dataCol1, dataCol2]]
            case '>':
                return self.dataSet[self.dataSet[dataCol1]-self.dataSet[dataCol2] > threshold][[dataCol1, dataCol2]]
            case '>=':
                return self.dataSet[self.dataSet[dataCol1]-self.dataSet[dataCol2] >= threshold][[dataCol1, dataCol1]]
            case  '<=':
                return self.dataSet[self.dataSet[dataCol1]-self.dataSet[dataCol2] <= threshold][[dataCol1, dataCol2]]
            case '==':
                return self.dataSet[self.dataSet[dataCol1]-self.dataSet[dataCol2] == threshold][[dataCol1, dataCol2]]
            case '!=':
                return self.dataSet[self.dataSet[dataCol1]-self.dataSet[dataCol2] != threshold][[dataCol1, dataCol2]]
            case _:
                raise ValueError(f'Invalid operator {opt}')

    def getQuarterlyDistribution(self, data: object, column: str):
        data.set_index("date", inplace=True)
        quarter_data = data[column].resample("Q").mean().reset_index()
        print(f'Quarter distribution of pirce according to column {column}\n', quarter_data.tail(20))
        vana.visuals.line(x='date', y=column, data=quarter_data.tail(20))
    
    def getCorrelation(self, data: object, col1: str, col2: str):
        print(f'Correlation beteen {col1} and {col2}', data[col1].corr(data[col2]))
        vana.visuals.heat(matrix=data.corr(),cmap='coolwarm')