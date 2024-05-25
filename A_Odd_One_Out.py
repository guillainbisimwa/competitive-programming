def findElements(values):
    results = []
    for value in values:
        foundUnique = list(set(value))
        if value.count(foundUnique[0]) == 1:
            results.append(foundUnique[0])
        else:
            results.append(foundUnique[1])
    return results

n = int(input())
values = [list(map(int, input().split())) for _ in range(n)]
results = findElements(values)

# Print the results
for result in results:
    print(result)
