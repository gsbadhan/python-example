'''
Created on 19-May-2016

@author: gsingh
'''
from threading import Thread
import time

class employee(object):
    '''
    classdocs
    '''


    def __init__(self, firstname="", lastname=""):
        self.firstname = firstname;
        self.lastname = lastname;
        
    
    def show(self):
        print(self.firstname + ":" + self.lastname);
        time.sleep(2);
