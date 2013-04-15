'''
Created on 2013/04/14

@author: ym
'''

from math import *
from cmath import *
from sys import *
import numpy as np
import scipy as sp

def mydot(a,b):
    return np.dot(a,b)+a+b

def perm1(ev):
    return sorted(zip(ev,range(len(ev))),key=lambda x:abs(phase(x[0])),reverse=True)

def split1s(l,vp,v0,vm):
    if (l==[]): return [vp,v0,vm]
    if (len(l) < 2): 
        v0.append(l[0][1].real)
        return split1s(l[1:],vp,v0,vm)
    elif ((round(l[0][0].real+1,7)==0) and (round(l[1][0].real+1,7)==0)): 
        vp.append(l[0][1].real)
        vm.append(l[1][1].real)
        return split1s(l[2:],vp,v0,vm)
    elif  ((round(l[0][0].real+1,7)==0) or (round(l[0][0].real-1,7)==0)):
        v0.append(l[0][1].real)
        return split1s(l[1:],vp,v0,vm)
    else: 
        vp.append(l[0][1].real)
        vm.append(l[1][1].real)
        return split1s(l[2:],vp,v0,vm)

def split1(ev):
    return split1s(ev,[],[],[])

def eigenvalues1(m):
    eg = np.linalg.eig(m)
    ev = eg[0]
    el = split1(perm1(ev))
    print el[0]
    print ev
    return [map(lambda x:phase(ev[x]),el[0]),map(lambda x:ev[x].real,el[1])]

def eigenvectors1(m):
    eg = np.linalg.eig(m)
    ev = eg[0]
    sl = split1(perm1(ev))
    evc= eg[1].T
    ev0 = map(lambda x:evc[x].real.tolist()+evc[x].imag.tolist(),sl[0])
    ev1 = map(lambda x:evc[x].tolist(),sl[1])
    return np.matrix(reduce(lambda a,b:a+b,ev0,[])+reduce(lambda a,b:a+b,ev1,[])).T

def diag1(l):
    sl=l[0]
    ol=l[1]
    ml=map(lambda x:matrix([[cos(x),-sin(x)],[sin(x),cos(x)]]),sl)
    nl=map(lambda x:matrix([[x]]),ol)
    
if __name__ == '__main__':
    a = np.array([[1,2],[3,4]])
    b = np.array([[5,6],[7,8]])
    print a
