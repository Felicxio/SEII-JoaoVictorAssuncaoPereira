import numpy as np

a = np.random.random((3,2))
print(a)

a= np.random.randn(1000)
print(a.mean(), a.var())

a = np.random.randint(10, size=(3,3))
print(a)


a = np.random.choice(5, size=10)
print(a)

a = np.random.choice([-8,-2,-5], size = 10)
print(a)
