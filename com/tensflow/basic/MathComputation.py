'''
Created on 25-Aug-2018

'''
import tensorflow as tf

'''
sample: out=f*(((a*b)/c)-d)

'''

def exampleA():
    a=tf.constant(3.0)
    b=tf.constant(5.0)
    c=tf.constant(4.0)
    d=tf.constant(2.0)
    f=tf.constant(2.0)
    result= f*(((a*b)/c)-d);
    sess= tf.Session()
    print(sess.run(result))
    sess.close()

def exampleB():
    a=tf.placeholder(tf.float32)
    b=tf.placeholder(tf.float32)
    c=tf.placeholder(tf.float32)
    d=tf.placeholder(tf.float32)
    f=tf.placeholder(tf.float32)
    result= f*(((a*b)/c)-d);
    sess= tf.Session()
    print(sess.run(result,{a:3.0,b:5.0,c:4.0,d:2.0,f:2.0}))
    sess.close()

if __name__ == '__main__':
    exampleA()
    exampleB()
    
    pass