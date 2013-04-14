'''
Created on 2013/04/14

@author: ym
'''
import scipy 
import scipy.linalg
from numpy import *

a = [ [1,3,5], [2,5,1], [2,3,8]]
A = mat(a)
print A.shape
print A.dtype
print "matrix->list", A.tolist()
print "Inverse:" , A.I
print "Hermite:", A.H
print "Transpose:", A.T
print "Matrix->Array:", A.A
print "Matrix->1dimAarray:", A.A1
print "second row:", A[1]
print "second column:", A.T[1]
print "Conjugate:", A.conj()
print "Diagonalization:", A.diagonal()
print "Determinant:", linalg.det(A)
print "Eigenvalues/Eigenvectors:", linalg.eig(A)
print "Normalize:", linalg.norm(A)
#print "LU fact", linalg.lu(A)
print "QR fact", linalg.qr(A)
print "Calculus"
print "A + A:", A+A
print "A - A:", A-A
print "A * A:", A*A
print "A / A:", A/A
print "A * A^-1", A*A.I
