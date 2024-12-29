def zero_delta(t, test_cases):

    results = []

    for n, k, arr in test_cases:
        for i in range(n - 1):
            move = min(k, arr[i])
            arr[i] -= move
            arr[-1] += move
            k -= move
            if k == 0:
                break
        
        results.append(arr)
    
    return results

def main():
    t = int(input())
    test_cases = []
    for _ in range(t):
        n, k = map(int, input().split())
        arr = list(map(int, input().split()))
        test_cases.append((n, k, arr))
    
    results = zero_delta(t, test_cases)
    
    for res in results:
        print(" ".join(map(str, res)))

if __name__ == "__main__":
    main()
