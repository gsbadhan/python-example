'''
Created on 25-Aug-2018

'''
import pandas as pd

if __name__ == '__main__':
    
# dataframe 
    data = {"Day":[1, 2, 3, 4, 5, 6, 7], "tarffic":[100, 290, 189, 1879, 189, 190, 188]}
    df = pd.DataFrame(data);
    print(df)
    
    # set day as index
    df.set_index("Day",inplace=True);
    print(df)
    
    # rename column
    df=df.rename(columns={"Day":"week day"})
    print(df)
    
    
    pass
