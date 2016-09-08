# Matrix Algebra

import numpy as np

A = np.array([[1, 2, 3],[1, 7, 4]])
B = np.array([[1, -1],[0, 1]])
C = np.array([[5, -1],[9, 1],[6, 0]])
D = np.array([[3, -2, -1],[1, 2, 3]])
u = np.array([[6, 2, -3, 5]])
v = np.array([[3, 5, -1, 4]])
w = np.array([[1],[8],[0],[5]])

"""
1. Matrix Dimensions
Write the dimensions of each matrix. 
"""

# 1.1) A
print A.shape
# 1.2) B
print B.shape
# 1.3) C
print C.shape
# 1.4) D
print D.shape
# 1.5) u
print u.shape
# 1.6) w
print w.shape

"""
2. Vector Operations
Perform the following operations. Assume a = 6
"""

alpha =  6

# 2.1)
print u + v
# 2.2)
print u - v
# 2.3)
print alpha * u
# 2.4)
print np.inner(u, v)
# 2.5)
print np.linalg.norm(u)

"""
3. Matrix operations
"""

# 3.1)
try:
	A + C
except ValueError:
	print "not defined"
# 3.2)
print A - C.transpose()
# 3.3)
print C.transpose() + (3 * D)
# 3.4)
print np.dot(B, A)
# 3.5)
try:
	np.dot(B, A.transpose())
except:
	print "not defined"

