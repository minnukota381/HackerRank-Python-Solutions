# Enter your code here. Read input from STDIN. Print output to STDOUT
A= set(map(int,input().split()))
n=int(input())
b=True
for i in range(n):
    ss=set(map(int,input().split()))
    
    if not A > ss:
        b=False
        
print(b)