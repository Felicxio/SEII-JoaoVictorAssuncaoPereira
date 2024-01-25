import numpy as np

#a = np.array([[1,2], [3,4]])
#eigenvalues , eigenvectors = np.linalg.eig(a)


#b = eigenvectors[:, 0] * eigenvalues[0]
#print(b)

#c= a@ eigenvectors[:, 0]
#print(b)

#print(np.allclose(b,c))

A = np.array([[1,1], [1.5, 4.0]])
b = np.array([2200,5050])

x = np.linalg.inv(A).dot(b)
print(x)

x = np.linalg.solve(A, b)
print(x)