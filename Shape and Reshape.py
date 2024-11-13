import numpy as np

arr = list(map(int, input().split()))

nArray = np.array(arr)
reshaped_array = np.reshape(nArray, (3, 3))
print(reshaped_array)