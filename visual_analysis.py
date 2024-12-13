import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

class visuals:
    def bar(dataSet: object, xVal: str, yVal: str):
        data_frame = pd.DataFrame({

        })
        sns.barplot(data=dataSet,x=xVal,y=yVal)
        plt.show()

    def histo(dataSet: object, label:str):
        sns.histplot(data=pd.DataFrame({label: sorted(dataSet)}), x=label)
        plt.show()