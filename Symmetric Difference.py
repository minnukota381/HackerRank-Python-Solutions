# Enter your code here. Read input from STDIN. Print output to STDOUT
Q=int(input())
Qu=set(map(int,input().split()))
R=int(input())
Ru=set(map(int,input().split()))

for He in sorted(Qu.symmetric_difference(Ru)):
    print(He)