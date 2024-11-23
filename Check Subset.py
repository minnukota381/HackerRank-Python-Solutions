# Enter your code here. Read input from STDIN. Print output to STDOUT
c=int(input())
for i in range(c):
    Q=int(input())
    Qu=set(map(int,input().split()))
    
    R=int(input())
    Ru=set(map(int,input().split()))
    
    print(Qu.issubset(Ru))