# -*- coding: utf-8 -*-
"""
create on Tue Nov 7 2017

@autor:allen

function:example1 of tensorflow
"""

import tensorflow as tf
hello = tf.constant('Hello, TensorFlow')#定义一个字符常量
sess = tf.Session()
#tensorflow以来一个高效的c++后端来进行计算。与后端的这个连接叫做session。我的理解是运行的是c++后端，而python需要将模型传送过去，首先是建立一个与后端连接的会话。有点类似网络中，并且这个连接是稳定的连接
#一般来说，使用tensorflow程序的流程是先建立一个图，然后在session中启动它
print sess.run(hello)
