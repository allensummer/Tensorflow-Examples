# -*- coding: utf-8 -*-
"""
create on Tue Nov 7 2017

@autor:allen

function:Addiction with two constans using tensorflow
"""
import tensorflow as tf
a = tf.constant(2)#定义一个常量
b = tf.constant(3)
sess = tf.Session()#连接session
print "a=2, b=3"
print "两个常量相加:%i"% sess.run(a + b)#启动图
print "两个常量相乘: %i" % sess.run(a * b)#启动图
#result
#两个常量相加：5
#两个常量相乘：6
