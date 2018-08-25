'''
Created on 25-Aug-2018

'''
import pandas as pd

if __name__ == '__main__':
    # convert csv file to html
    users=pd.read_csv("user.csv", index_col=0);
    users.to_html("user.html")
    
    pass
