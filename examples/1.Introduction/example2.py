# -*- coding: utf-8 -*-
"""
create on Tue Nov 7 2017

@autor:allen

function:example2 of tensorflow
"""
import tensorflow as tf
a = tf.constant(2)#定义一个常量
b = tf.constant(3)
sess = tf.Session()#连接session
print "a=2, b=3"
print "Addition with constants:%i"% sess.run(a + b)#启动图
print "multiplication with constans: %i" % sess.run(a * b)#启动图

