def swap(n, s):

    max_ops = 0
    for i in range(n - 1):
        if s[i] == 'A' and s[i + 1] == 'B':
            max_ops += 1
    return max_ops
    

n = int(input())
s = input()

swap(n, s)