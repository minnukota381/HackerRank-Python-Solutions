# Enter your code here. Read input from STDIN. Print output to STDOUT
N,X = map(int,input().split())
listS=[]
for i in range(X):
    l=list(map(float,input().split()))
    listS.append(l)
        
zm = zip(*listS)

for stm in zm:
    tot = sum(stm)
    avg = tot / X
    print(f"{avg:.1f}")