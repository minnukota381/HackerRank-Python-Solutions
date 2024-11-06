# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(input())
countries = set()
for i in range(N):
    country = input()
    countries.add(country)
    
print(len(countries))