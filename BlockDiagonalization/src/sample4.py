'''
Created on 2013/04/15

@author: ym
'''
from math import *
from cmath import *
from sys import *
import numpy as np
import scipy as sp
import BlockDiagonalization as bd

def rm(theta):
    return np.matrix([[cos(theta),-sin(theta),0], [sin(theta),cos(theta),0], [0,0,1]])

x1 = rm(pi/4)
eg = np.linalg.eig(x1)
el = eg[0]
print x1.real
print x1.imag
print el.imag
print np.matrix([abs(el.imag),range(len(el))]).T
print bd.perm1(el)
print bd.eigenvalues1(x1)

x1 = rm(pi)
eg = np.linalg.eig(x1)
el = eg[0]
print np.real_if_close(bd.perm1(el))
print bd.split1(bd.perm1(el))
print bd.eigenvalues1(x1)


x1 = rm(pi/4)
eg = np.linalg.eig(x1)
el = eg[0]
ev = np.matrix(eg[1]).T
print "x",np.around(x1,decimals=3)
print "el",np.around(np.matrix(el),decimals=3)
print "ev",ev
print "diag?",np.around(np.dot(ev,np.dot(x1,ev.T)),decimals=3)
print "orthogonal?", np.around(np.dot(ev.H,ev),decimals=3)
print "ev[0].x1",np.dot(ev[0],x1)
print "ev[0]",ev[0]

