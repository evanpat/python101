import numpy as np

# create ndarray
arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(type(arr))
print(arr[1])

# vs python list
arr1 = [1,2,3,4,5]
print(arr1)
print(type(arr1))

# n-dimension array
a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim, a.shape)
print(b.ndim, b.shape)
print(c.ndim, c.shape)
print(d.ndim, d.shape)
print("c[1, 2]=", c[1, 2])
print("d[0, 0, 2]=", d[0, 0, 2])

print(d)

# slicing
arr2 = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr2[1:5])
i=4
print(arr2[:i], arr2[i:])


arr3 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

newarr = arr3.reshape(2, 3, 2)
print(newarr)
print(newarr.shape)
