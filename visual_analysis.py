import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

class visuals:
    def bar(dataSet: object, xVal: str, yVal: int, rotation: int | None):
        plt.figure(figsize=(10,10))
        sns.barplot(data=dataSet,x=xVal,y=yVal)
        if rotation is not None:
            plt.xticks(rotation=rotation)
        plt.show()

    def histo(dataSet: object, label:str):
        sns.histplot(data=pd.DataFrame({label: sorted(dataSet)}), x=label)
        plt.show()

    def line(x: str, y: str, data: object, hue:str | None = None, rotation: int | None = None):
        if hue is not None:
            sns.lineplot(x=x, y=y, hue=hue, data=data)
        else:
            sns.lineplot(x=x, y=y, data=data)
        if rotation is not None:
            plt.xticks(rotation=rotation)
        plt.show()

    def heat(matrix: object, cmap: str ,annot: bool = False):
        plt.figure(figsize=(10,10))
        sns.heatmap(matrix, annot=annot, cmap=cmap)
        plt.show()