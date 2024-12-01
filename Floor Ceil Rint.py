# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np
np.set_printoptions(legacy='1.13')

FCR = np.array(list(map(float,input().split())))

print(np.floor(FCR))
print(np.ceil(FCR))
print(np.rint(FCR))