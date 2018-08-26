'''
Created on 26-Aug-2018

'''
import numpy as np

if __name__ == '__main__':
    
    ar1 = np.array([1, 2, 3, 4, 5]);
    ar2 = np.array([6, 7, 8, 9, 10]);
 
#     add/subtract/multiply/divide two arrays
    print(ar1 + ar2);
    print(ar1 - ar2);
    print(ar1 * ar2);
    print(ar1 / ar2);
    
    ar2d = np.array([[10, 12, 13, 14], [15, 16, 17, 18]])
#     slicing
    print(ar2d[0:,0:2])
    print(ar2d[0:,2:4])
    
#     maximum from array
    print(ar2d.max())
    
    #     minimum from array
    print(ar2d.min())
    
    #     sum from array
    print(ar2d.sum())
    
#     flat array
    print(ar2d.ravel())
    
    # shape
    print(ar2d.shape)
    
    pass
