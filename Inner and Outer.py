# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np

k=list(map(int,input().split()))
b=list(map(int,input().split()))

A=np.array(k)
B=np.array(b)

print(np.inner(A, B))
print(np.outer(A, B))