def construct_skyscrapers(n, limits):
    floors = [0] * n

    floors[0] = limits[0]

    for i in range(1, n):
        floors[i] = min(limits[i], floors[i - 1])

    return floors

n = int(input().strip())
limits = list(map(int, input().strip().split()))

result = construct_skyscrapers(n, limits)

print(*result)
