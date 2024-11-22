def mutate_string(s, pos, ch):
    return s[:pos]+ch+s[pos+1:]

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)