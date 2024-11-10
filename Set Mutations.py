# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
A=set(map(int, input().split()))
N=int(input())

for x in range(N):
    cmd = input().split()
    B = set(map(int, input().split()))
    if cmd[0] == "intersection_update":
        A.intersection_update(B)
    if cmd[0] == "update":
        A.update(B)
    if cmd[0] == "symmetric_difference_update":
        A.symmetric_difference_update(B)
    if cmd[0] == "difference_update":
        A.difference_update(B)

print(sum(A))