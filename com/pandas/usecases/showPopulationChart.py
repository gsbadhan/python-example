'''
Created on 25-Aug-2018

'''
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
style.use('fivethirtyeight');

if __name__ == '__main__':
    df=pd.read_csv("population-data.csv", index_col=0)
    df=df.set_index(["country"])
    print(df)
    df.plot(kind='bar')
    plt.show()
    pass
