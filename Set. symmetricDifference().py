# Enter your code here. Read input from STDIN. Print output to STDOUT

E = int(input())
Eng = set(map(int,input().split()))
F=int(input())
French= set(map(int,input().split()))
print(len(Eng.symmetric_difference(French)))