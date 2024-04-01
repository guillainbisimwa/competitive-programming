def bounce(x, skillfull):
    bounces = 0
    distance = 0

    for i in skillfull:
        distance += i
        if distance <= x:
            bounces += 1
        else:
            break
    return bounces+1

n, x = map(int, input().split())

skillfull = list(map(int, input().split()))

print(bounce(x, skillfull))