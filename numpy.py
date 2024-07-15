# numpy functionalities and usage
import numpy as np
import pandas as pd

# \/-axis=0, ->-axis=1
a = np.array([[1, 2, 3], [4, 5, 6]])

print(a.shape)

a = np.array([1, 2, 3, 4, 5, 6])
print(a)
# mutable:
a[0] = 10
print(a)
# slicing
print(a[:3])

a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

print(f"\n{a}")
# [row, column]
print(f'{a[0, 2]}\n')

# ARRAY ATTRIBUTES
print(a.ndim)
print(a.size)
print(f'a.dtype\n')

# HOW TO CREATE BASIC ARRAYS
print(np.zeros(2))
print(np.ones(2))
print(np.empty(2))  # we just define the size, the content is random
print(np.arange(4))  # create an array with a range of elements
print(np.arange(2, 9, 2))
print(f'{np.linspace(0, 10, num=5)}\n')

x = np.ones(2, dtype=np.int32)
print(f'{x}, {x.dtype}\n')

# Adding, removing, and sorting elements
arr = np.array([2, 1, 5, 3, 7, 4, 6, 8])
print(f'{np.sort(arr)}\n')
a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])
print(f'{np.concatenate((a, b))}\n')
x = np.array([[1, 2], [3, 4]])
y = np.array([[5, 6]])
print(f'{np.concatenate((x, y), axis=0)}\n')

# RESHAPE
a = np.arange(6)
print(f'{a.reshape(2, 3)}\n')

# Add a new axis to an array
a = np.array([1, 2, 3, 4, 5, 6])
print(a.shape)
print(a[np.newaxis, :].shape)
print(f'{a[:, np.newaxis].shape}\n')
print(np.expand_dims(a, axis=0).shape)
print(f'{np.expand_dims(a, axis=1).shape}\n')

# Indexing and slicing
a = np.array([1, 2, 3])
print(a[-2:])
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(a[a < 10])
five_up = (a >= 5)
print(a[five_up])
divisible_by_2 = a[a % 2 == 0]
print(divisible_by_2)
c = a[(a < 2) | (a > 11)]  # & and |
print(c)
print((a > 5) & (a == 7))
print(np.nonzero(a < 10))
'''a tuple of arrays was returned: one for each dimension. 
The first array represents the row indices where these values are found, 
and the second array represents the column indices where the values are found.'''

# How to create an array from existing data
a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
a1 = a[3:8]
print(a1)
a1 = np.array([[1, 1], [2, 2]])
a2 = np.array([[3, 3], [4, 4]])
print(np.vstack((a1, a2)))  # vertical stack
print(np.hstack((a1, a2)))  # horizontal stack
x = np.arange(1, 25).reshape(2, 12)
print(x)
print(np.hsplit(x, 3))  # split an array into 3 equal
print(np.hsplit(x, (3, 4)))  # split an array after 3 and 4 columns
print()
# so-called "view" in python, creates new array that looks the same,
# however modification of "view" modifies initial array
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
# b2 = a.copy() # copy function allows to create a full copy that will not modify initial array
# b1 = b2[0, :]
b1 = a[0, :]
print(b1)
b1[0] = 99
print(b1)
print(a)

# Basic array operations
data = np.array([1, 2])
ones = np.ones(2, dtype=int)
print(data + ones)
print(data - ones)
print(data * ones)
print(data / ones)
print(data // ones)
print(data % ones)
a = np.arange(0, 10)
print(a.sum())
b = np.array([[1, 2], [3, 4]])
print(b.sum(axis=0))
print(b.sum(axis=1))

# Broadcasting
data = np.array([1., 2.])
print(data * 1.6)

a = np.array([[0.45053314, 0.17296777, 0.34376245, 0.5510652],
              [0.54627315, 0.05093587, 0.40067661, 0.55645993],
              [0.12697628, 0.82485143, 0.26590556, 0.56917101]])
print(a.sum())
print(a.min())
print(a.min(axis=0))  # will find min in each column
print(a.min(axis=1))  # will find min in each row
print(a.max())

# Generating random numbers
rng = np.random.default_rng()
print(rng.integers(510, size=(2, 4)))
print()

# How to get unique items and counts
a = np.array([11, 11, 12, 13, 14, 15, 16, 17, 12, 13, 11, 14, 18, 19, 20])
print(np.unique(a))
print(np.unique(a, return_index=True))
print(np.unique(a, return_counts=True))
# works also for 2D arrays

# Transposing and reshaping a matrix
data = np.arange(1, 7)
print(data.reshape(2, 3))
print(data.reshape(3, 2))
data = data.reshape(3, 2)
print(data.transpose())
print(data.T)
print()

# How to reverse an array
print(np.flip(np.arange(7)))
a = np.arange(1, 13).reshape(3, 4)
print(np.flip(a))
print(np.flip(a, axis=0))
print(np.flip(a, axis=1))
a[1] = np.flip(a[1])
print(a)
a[:, 1] = np.flip(a[:, 1])
print(f'{a}\n')

# Reshaping and flattening multidimensional arrays
x = np.arange(1, 13).reshape(3, 4)
a = x.flatten()   # won't change initial array
a[1] = 99
print(x)
print(a)
a_change = x.ravel()  # will change initial array
a_change[1] = 99
print(x)
print(f'{a_change}\n')

