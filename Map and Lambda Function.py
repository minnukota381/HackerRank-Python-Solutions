cube = lambda x:x**3 # complete the lambda function 

def fibonacci(n):
    # return a list of fibonacci numbers
    if n==0:
        return []
    if n==1:
        return [0]
    if n==2:
        return [0,1]
    
    lis=[0,1]
    for i in range(2,n):
        lis.append(lis[i-1]+lis[i-2])
    return lis
    

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))