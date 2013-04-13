'''
Created on 2013/04/14

@author: ym
'''
from math import *
from cmath import *
import numpy as np
import scipy as sp
# import BlockDiagonalization as Bd

if __name__ == '__main__':
    pi=3.141592
    a = np.matrix([[cos(pi/3),-sin(pi/3)],[sin(pi/3),cos(pi/3)]])
    b = np.linalg.eig(a)
#    print Bd.mydot(a,b)
#    print dot(a,b)
    print a
    print b[0]
    print b[1]
    print b[1][0,1]
    print phase(b[1][0,1])/pi