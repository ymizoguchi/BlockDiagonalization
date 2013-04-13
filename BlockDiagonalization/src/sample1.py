'''
Created on 2013/04/14

@author: ym
'''
import numpy
from  scipy import *
import BlockDiagonalization as Bd

if __name__ == '__main__':
    a = array([[1,2],[3,4]])
    b = array([[5,6],[7,8]])
    print Bd.mydot(a,b)
    print dot(a,b)