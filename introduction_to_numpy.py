# -*- coding: utf-8 -*-
"""Introduction to Numpy.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ioI5HLX7N7OfrhRNPrYPM3AvJCcAJJBu
"""

import numpy as np

a = np.array([1,2,3,4])
print(a)

a.ndim

b = np.array([[1,2,3],[4,5,6]])
print(b)

b.ndim

c = np.array([[[1,2,3],[4,5,6]]])
print(c)

c.ndim

d = np.array([1,2,3,4], ndmin = 4)
print(d)

d.dtype

e = np.array([[[1,2,3],[4,5,6]]], dtype = 'int32')

e.dtype

f = np.array([[1,2,3,4],[4,5,6,7]])

print(f)

f.shape

array = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
new_array = array.reshape(4,3)
print(new_array)

array1 = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
new_array1 = array1.reshape(2,3,2)
print(new_array1)

arr_error = np.array([1,2,3,4,5,6,7,8])
newarr_error = arr_error.reshape(2,4)
print(newarr_error)



"""Accessing/ Changing Specific elements, rows, columns"""

m = np.array([[1,2,3,4,5,6,7,8],[9,10,11,12,13,14,15,16]])
print(m)



"""m[r,c]"""

m[0,2]

m[1,6]

m[1,:]

m[:,3]

dim = np.array([1,2,3,4,5,6,7,8,9,10])
new_dim = dim.reshape(2,5)
print(new_dim)

m = np.array([[1,2,3,4,5,6,7,8],[9,10,11,12,13,14,15,16]])
print(m)

m[0,2] = 50

print(m)

m[1,1] = 40

print(m)

"""Basic Maths"""

t = np.array([1,2,3,90])
print(t)

t +2

t-2

t ** 4

np.sin(t)

np.cos(t)

np.min(t)

np.max(t)

np.mean(t)

import time
import sys

List = range(500)
print(sys.getsizeof(5)*len(List))

Array = np.arange(500)
np.size(Array)

