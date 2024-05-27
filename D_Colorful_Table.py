def process_intervals_and_print_results(n):
    results = []

    for _ in range(n):
        m, k = map(int, input().split())
        
        r = float('-inf')
        l = float('inf')
        ans = [0] * (k + 1)
        
        x = list(map(int, input().split()))
        index_x = [(x[i], i) for i in range(m)]
        index_x.sort(reverse=True)
        
        for x, i in index_x:
            l = min(l, i)
            r = max(r, i)
            ans[x] = 2 * (r - l + 1)
        
        results.append(ans[1:]) 
        # results.append(ans[:1]) 
        # Exclude the 1st element as it is unused !!!
    
    for result in results:
        print(" ".join(map(str, result)))

n = int(input())

process_intervals_and_print_results(n)
