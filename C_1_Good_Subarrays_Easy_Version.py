def calculate_ans(test_cases):
    results = []
    for n, arr in test_cases:
        l = 0
        ans = 0
        for r in range(n):
            while arr[r] < (r - l + 1):
                l += 1
            ans += r - l + 1
        results.append(ans)
    return results

# Main function
if __name__ == "__main__":
    t = int(input())
    test_cases = []
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        test_cases.append((n, arr))
    
    results = calculate_ans(test_cases)
    for ans in results:
        print(ans)
