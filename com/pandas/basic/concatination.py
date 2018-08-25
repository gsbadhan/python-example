'''
Created on 25-Aug-2018

'''
import pandas as pd

if __name__ == '__main__':
    
# dataframe 
    df1 = pd.DataFrame({"Day":[1, 2, 3, 4], "tarffic":[100, 290, 189, 1879]})
    df2 = pd.DataFrame({"Day":[ 5, 6, 7], "tarffic":[ 189, 190, 188]})
    print(df1)
    print(df2)
    
    df3=pd.concat([df1,df2])
    print(df3)
    
    
    pass
