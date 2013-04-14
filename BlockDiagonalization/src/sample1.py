'''
Created on 2013/04/14

@author: ym
'''
from math import *
from cmath import *
from sys import *
import numpy as np
import scipy as sp
# import BlockDiagonalization as Bd

if __name__ == '__main__':
#    pi=3.141592
    eps = float_info.epsilon
    a = np.matrix([[cos(pi/3),-sin(pi/3)],[sin(pi/3),cos(pi/3)]])
    b = np.linalg.eig(a)
#    print Bd.mydot(a,b)
#    print dot(a,b)
    print pi
    print a
    print b[0]
    print b[1]
    print b[1][1,1]
    print phase(b[1][1,1])/pi
    print b[1][1,1]* 1j
    print np.real_if_close(b[1][1,1]* 1j )
    print np.around(b[1],decimals=3)
    print (abs(b[1][1,1]))
    