import numpy as np

x = np.array([1,2,3])
b = x.copy()
b[0] = 42
print(b)
print(x)