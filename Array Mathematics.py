import numpy as np

k, m = map(int, input().split())
A = []
B = []
for i in range(k):
    A.append(list(map(int, input().split())))

for i in range(k):
    B.append(list(map(int, input().split())))

A = np.array(A)
B = np.array(B)

print(np.add(A, B))
print(np.subtract(A, B))
print(np.multiply(A, B))
print(np.divide(A, B).astype(int))
print(np.mod(A, B))
print(np.power(A, B))
