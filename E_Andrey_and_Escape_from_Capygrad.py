def portal(n):
    results = []

    for _ in range(n):
        m = int(input())
        
        setPortals = []
        for __ in range(m):
            portal = [int(i) for i in input().split()]
            setPortals.append(portal)
        
        q = int(input())
        X = [int(x) for x in input().split()]
        
        for x in X:
            setPortals.append([x, x, x, x])
        
        setPortals.sort(key=lambda i: -i[3])
        
        j = 0
        qans = {}
        
        for l, r, a, b in setPortals:
            while b < setPortals[j][0]:
                j += 1
            qans[b] = qans.get(setPortals[j][3], b)
        
        result = [qans[x] for x in X]
        results.append(result)
    
    return results

# Input reading and function calling
n = int(input())
results = portal(n)

# Print the results
for result in results:
    print(' '.join(map(str, result)))
