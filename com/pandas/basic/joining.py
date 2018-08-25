'''
Created on 25-Aug-2018

'''
import pandas as pd

if __name__ == '__main__':
    
# dataframe 
    df1 = pd.DataFrame({"bank":['icici', 'citi', 'swiss', 'BOK','PNB'], "FD interest rate":[6.5, 7, 6.7, 5,7.7]},index=[2001,2001,2001,2001,2001])
    df2 =  pd.DataFrame({"country":['india', 'usa', 'japan', 'africa'], "no. account":[9000, 7000, 3000, 4500]},index=[2001,2001,2001,2001])
    print(df1)
    print(df2)
    
    # join two dataframes based on index
    joinOut = df1.join(df2)
    print(joinOut)
    
    
    pass
