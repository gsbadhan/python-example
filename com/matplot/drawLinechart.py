'''
Created on 25-Aug-2018

'''

from matplotlib import pyplot as plt

if __name__ == '__main__':
    
    x1=[1,3,2,1]
    y1=[4,5,6,7]
    x2=[2,4,3,2]
    y2=[1,2,3,4]
    
    plt.plot(x1,y1,'g',label="trend",linewidth=3);
    plt.plot(x2,y2,'g',label="trend",linewidth=3);
    plt.title("sample")
    plt.xlabel("x axis")
    plt.ylabel("y axis")
    
    plt.legend()
    plt.grid(True)
    
    plt.show()
    pass