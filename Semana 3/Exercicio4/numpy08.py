import numpy as np

a = np.array([[10,19,30,41,50,61]])
#print(a)

#b= a[0,1]
#print(b)

#print(a)
#bool_idx = a>2
#print(bool_idx)
#print(a[a>2])

#b = np.where (a>2, a , -1)
#print(b)

print(a)
even = np.argwhere(a%2==0).flatten()
print(a[even])

