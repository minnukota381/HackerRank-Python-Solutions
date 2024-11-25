# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations

S,k=input().split()
k = int(k)
j= permutations(S,k)

strlist = []

for p in j:
    j_str = ''.join(p)
    strlist.append(j_str)
s_per = sorted(strlist)

print("\n".join(s_per))
