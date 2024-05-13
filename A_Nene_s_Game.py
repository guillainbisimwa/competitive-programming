t = int(input())
for _ in range(t):
    k, q = map(int, input().split())
    arr = list(map(int, input().split()))
    queries = list(map(int, input().split()))
    for a in queries:
        if a < arr[0]:
            print(a, end=" ")
        else:
            print(arr[0] - 1, end=" ")
    print()