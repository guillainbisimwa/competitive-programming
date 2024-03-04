def calculate_total(n, coordinates):
    d = {}
    for x, y in coordinates:
        if x not in d:
            d[x] = []
        d[x].append(y)
    res = 0
    for i in d:
        d[i].sort(reverse=True)
        res += sum(d[i][:i])
    return res

t = int(input())
for _ in range(t):
    n = int(input())
    coordinates = [map(int, input().split()) for _ in range(n)]
    total = calculate_total(n, coordinates)
    print(total)

# throws Time limit exceeded on test 3
