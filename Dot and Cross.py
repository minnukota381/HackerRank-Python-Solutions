# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np

n= int(input())
A=[]
B=[]
for i in range(n):
    A.append(list(map(int,input().split())))
    
for i in range(n):
    B.append(list(map(int,input().split())))

A=np.array(A)
B=np.array(B)

print(np.dot(A,B))