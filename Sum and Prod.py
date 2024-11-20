# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np

n,m=map(int,input().split())

arr=[]

for i in range(n):
    s=list(map(int,input().split()))
    arr.append(s)
    
arr=np.array(arr)

arrSum = np.sum(arr, axis=0)
arrPro = np.prod(arrSum)

print(arrPro)