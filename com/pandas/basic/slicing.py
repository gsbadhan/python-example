'''
Created on 25-Aug-2018

'''
import pandas as pd

if __name__ == '__main__':
    
# dataframe 
    data = {"Day":[1, 2, 3, 4, 5, 6, 7], "tarffic":[100, 290, 189, 1879, 189, 190, 188]}
    df = pd.DataFrame(data);
    print(df)
    
#     slice top rows
    print(df.head(3))
    
#     slice last rows
    print(df.tail(3))
    
    
    pass
