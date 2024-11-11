# Enter your code here. Read input from STDIN. Print output to STDOUT
T= int(input())
for i in range(T):
    try:
        ls=list(map(int,input().split()))
        f=ls[0]//ls[1]
        print(f)
    except ZeroDivisionError as e:
        print("Error Code:", e)
    except ValueError as e:
        print("Error Code:", e)