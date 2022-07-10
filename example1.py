from mathfun.ops import basic
import numpy as np 
from mathfun.arrays.basic import add_arr

c = basic.add1(12,13)
print(c)

divdif = basic.DiffandDiv()

c = divdif.diff(12,4)
print(c)

c = divdif.divide(12,4)
print(c)

a = np.array([2,3])
b = np.array([4,5])

c = add_arr(a,b)
print(a, " + ", b, " = ", c)
