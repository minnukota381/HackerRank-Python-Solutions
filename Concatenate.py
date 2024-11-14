# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np
n, m, p = map(int, input().split())

array_1 = []
array_2 = []

for i in range(n):
    row = list(map(int, input().split()))
    array_1.append(row)

for j in range(m):
    row = list(map(int, input().split()))
    array_2.append(row)

array_1 = np.array(array_1)
array_2 = np.array(array_2)

result = np.concatenate((array_1, array_2), axis=0)

print(result)
