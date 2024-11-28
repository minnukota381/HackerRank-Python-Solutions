# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np

n,m = map(int,input().split())
arr=[]
for i in range(n):
    arr.append(list(map(int,input().split())))

a=np.array(arr)

print(np.mean(a, axis=1))
print(np.var(a, axis=0))
std_dev = np.std(a, axis=None)
print(round(std_dev, 11))