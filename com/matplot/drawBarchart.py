'''
Created on 25-Aug-2018

'''

from matplotlib import pyplot as plt

if __name__ == '__main__':
    
    x1=[1,3,2,1]
    y1=[4,5,6,7]
    x2=[2,4,3,2]
    y2=[1,2,3,4]
    
    plt.bar(x1,y1,label="trend",color='g')
    plt.bar(x2,y2,label="trend",color='y')
    plt.title("sample")
    plt.xlabel("x axis")
    plt.ylabel("y axis")
    
    plt.legend()
    
    plt.show()
    pass