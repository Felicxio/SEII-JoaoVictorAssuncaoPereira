import numpy as np

a = np.array([[1,2,3,2,5,6,2], [17,18,19,23,45,67,21]])
print(a)
print(a.mean(axis=1))
print(np.max(a, axis=None))