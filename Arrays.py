import numpy

def arrays(arr):
    # complete this function
    arr = numpy.array(arr, dtype=float)
    return arr[::-1]

arr = input().strip().split(' ')
result = arrays(arr)
print(result)