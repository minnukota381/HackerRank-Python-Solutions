if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    h=list(set(arr))
    h.sort()
    print(h[-2])
