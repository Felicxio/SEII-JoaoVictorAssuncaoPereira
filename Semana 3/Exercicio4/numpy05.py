import numpy as np

l1 = [1,2,3]
l2 = [4,5,6]
a1 = np.array(l1)
a2 = np.array(l2)

#dot product

dot = np.dot(a1,a2)
print(dot)

dot = a1 @ a2
print(dot)