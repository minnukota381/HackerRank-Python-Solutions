# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

n=int(input())
pattern = r"^[789]\d{9}$"

for i in range(n):
    strng=input().strip()
    
    if re.match(pattern, strng):
        print("YES")
    else:
        print("NO")
    