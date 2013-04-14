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

def rmatrix(a,theta):
    a[0,0]=cos(theta)
    a[0,1]=-sin(theta)
    a[1,0]=sin(theta)
    a[1,1]=cos(theta)

def r2matrix(theta):
    return np.matrix([[cos(theta),-sin(theta)],[sin(theta),cos(theta)]])

if __name__ == '__main__':
#    pi=3.141592
    eps = float_info.epsilon
    a=np.matrix([[1j,1j],[1j,1j]])
    rmatrix(a,pi/3)
    print a
    b=r2matrix(pi/3)
    print b
    c=r2matrix(pi/6)
    print c
    print b
    d=np.ones((3,2),dtype=complex)
    print d
#    b = np.linalg.eig(a)
#    p = b[1]
#    print np.around(b[0],decimals=3)
#    print np.around(np.dot(np.dot(p.H,a),p),decimals=3)
