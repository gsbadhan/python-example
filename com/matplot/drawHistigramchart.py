'''
Created on 25-Aug-2018

'''

from matplotlib import pyplot as plt

if __name__ == '__main__':
    
    ages=[10,12,78,90,50,45,20,34,56]
    bins=[0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100]
    
    plt.hist(ages,bins)
    plt.title("sample")
    plt.xlabel("x axis")
    plt.ylabel("y axis")
    
    plt.legend()
    
    plt.show()
    pass