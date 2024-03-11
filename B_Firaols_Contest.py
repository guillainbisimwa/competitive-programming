
def held_rounds(n, difficulties):
    pool = set()
    result = []

    for difficulty in difficulties:
        pool.add(difficulty)
        if len(pool) == n:
            result.append('1')
            pool.clear()
        else:
            result.append('0')

    return ''.join(result)

n, m = map(int, input().split())
difficulties = list(map(int, input().split()))

result = held_rounds(n, difficulties)
print(result)

