# -*- coding: utf-8 -*-
"""
create on Tue Nov 7 2017

@autor:allen

function:basic operate in tf:add, mul, matmul
"""

import tensorflow as tf
a = tf.placeholder(tf.int16)#占位符
b = tf.placeholder(tf.int16)#占位符
#a和b并不是特定的值，相反，他们都是占位符，可以在tensorflow运行某一计算时根据该占位符输入具体的值
#这里a,b是一个int16的值，还可以是一个2维的浮点数张量
add = tf.add(a, b)
#加法运算
#mul = tf.mul(a, b)
#乘法运算
sess = tf.Session()
print "2+3=%i" % sess.run(add, feed_dict={a:2, b:3})
#print "2*3=%i" % sess.run(add, feed_dict={a:2, b:3})
#现在我们可以在一个Session里面启动这个运算
#feed_dict这个是喂进这个sess中的参数列表。因为a,b全部是占位符，并不是真实的值，没有办法参与运算，必须要给这两个占位符赋值

mat1 = tf.constant([[4., 4.]])#定义一个二维张量
mat2 = tf.constant([[5.], [5.]])#定义一个二维张量

matmul = tf.matmul(mat1, mat2)#张量相乘
print "矩阵相乘:%i" % sess.run(matmul)
#result
#2+3=5
#矩阵相乘：40
