def swap_case(s):
    a=s.swapcase()
    return str(a)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)