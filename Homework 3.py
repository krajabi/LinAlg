
# coding: utf-8

# In[ ]:

import numpy as np
import sympy as sp
import pandas as pd


# In[ ]:

#problem 9 -- determinant
def get_determinant(Matrix M):
    X=input("Enter a matrix in [] format:")
    X = str(X)
    X = np.matrix(X)
    determinant_value = np.linalg.det(X)
return determinant_value


# In[ ]:

#problem 10 -- area of triangle

def distance(x,y):
    length = np.sqrt((x**2)+(y**2))
    return length

side1x = float(input('Value of point 1, x coordinate: '))
side1y = float(input('Value of point 1, y coordinate: '))
side1 = distance(side1x,side1y)

side2x = float(input('Value of point 2, x coordinate: '))
side2y = float(input('Value of point 2, y coordinate: '))
side2 = distance(side2x,side2y)

side3x = float(input('Value of point 3, x coordinate: '))
side3y = float(input('Value of point 3, y coordinate: '))
side3 = distance(side3x,side3y)

all_sides = (side1+side2+side3)/2
area = (all_sides*(all_sides-side1)*(all_sides-side2)*(all_sides-side3)) ** 0.5
print 'area of triangle= ' 
print(area)


# In[85]:

#problem11
A = np.matrix('4 3 2; 1 2 6; 5 8 1')
eigen = np.linalg.eig(A)
eigenvalues = np.linalg.eigvals(A)

