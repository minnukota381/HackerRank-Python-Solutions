# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy

n=int(input())
A=[]
for i in range(n):
    A.append(list(map(float,input().split())))
    
A=numpy.array(A)

print(round(numpy.linalg.det(A), 2))
