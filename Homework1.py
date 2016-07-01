from sympy import *
import numpy as np

#problem 8
A = Matrix([[1,2,3,4,5], [1,2,3,4,5], [1,2,3,4,5], [1,2,3,4,5], [1,2,3,4,5]])
A
A*A*A

#problem 9
A = Matrix([[2,4,5], [2,6,1], [-2,9,15], [12,0,15], [3,34,-52]])
B = Matrix([[2,4,5,4], [2,6,1,4], [-2,9,15,4]])
C = (A*B).T
C

#problem 10
M = Matrix([[2,4,5], [2,6,1], [-2,9,15], [12,0,15], [3,34,-52]])
np.rank(M)

#problem 11
M = Matrix([[1,0,1,3], [2,3,4,7], [-1,-3,-3,-4]])
M.rref()
#row echelon