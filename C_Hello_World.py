def can_form_sequence(p):
    results = []
    for n, c in p:
        c.sort()
        if c[0] != 1:
            results.append("NO")
            continue

        total = 1
        possible = True
        for i in range(1, n):
            if c[i] > total:
                possible = False
                break
            total += c[i]
        
        results.append("YES" if possible else "NO")
    return results

t = int(input())
p = [(int(input()), list(map(int, input().split()))) for _ in range(t)]

for result in can_form_sequence(p):
    print(result)
