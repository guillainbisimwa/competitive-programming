# Read the input values for n and d
n, d = map(int, input().split())

s = input()

if "0" * d in s:
    print(-1)
else:
    jumps = 0
    index = 0

    while index < n - 1:
        if s[index] == "1":
            index += d
            jumps += 1
        else:
            index -= 1  # gooooo  one step back???
    print(jumps)
