# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np

n,m = map(int,input().split())

arr=[]
for i in range(n):
    arr.append(list(map(int,input().split())))
    
arr=np.array(arr)

print(np.transpose(arr))
print(arr.flatten())