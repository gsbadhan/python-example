'''
Created on 19-May-2016

@author: gsingh
'''
from threading import Thread
from com.funniest.employee import employee

class Crawller(Thread):


    def __init__(self, employee):
        Thread.__init__(self);
        self.employee = employee;
        
    def run(self):
       while True:
           self.employee.show();
           

        
