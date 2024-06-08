def divide(n, q, a, queries):
    def f(i, j):
        r.add(sum(a[i:j]))
        k = i
        while k < j and 2 * a[k] <= a[i] + a[j - 1]:
            k += 1
        if k < j:
            f(i, k)
            f(k, j)

    r = {0}
    a.sort()
    f(0, n)
    
    results = []
    for s in queries:
        results.append("Yes" if s in r else "No")
    return results

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    t = int(data[index])
    index += 1
    results = []
    
    for _ in range(t):
        n = int(data[index])
        q = int(data[index + 1])
        index += 2
        a = list(map(int, data[index:index + n]))
        index += n
        queries = list(map(int, data[index:index + q]))
        index += q
        
        results.extend(divide(n, q, a, queries))
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
