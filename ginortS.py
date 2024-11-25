# Enter your code here. Read input from STDIN. Print output to STDOUT
S=input()
l=[]
u=[]
o=[]
e=[]

for i in S:
    if i.islower():
        l.append(i)
    if i.isupper():
        u.append(i)
    if i.isdigit():
        if int(i)%2==0:
            e.append(i)
        else:
            o.append(i)
l.sort()
u.sort()
o.sort()
e.sort()

k="".join(l+u+o+e)

print(k)