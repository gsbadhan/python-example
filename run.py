'''
Created on 19-May-2016

@author: gsingh
'''
from com.funniest.employee import employee
from com.bootstrap.Crawller import Crawller

if __name__ == '__main__':
    emp = employee("gurpreet","singh");
    crawl = Crawller(emp);
    crawl.start();
    pass