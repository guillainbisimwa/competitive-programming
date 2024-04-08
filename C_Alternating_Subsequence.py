def max_alternating_sum():
    n = int(input())
    ans = 0
    now = -1
    v1 = -1e9
    v2 = 0
    a = list(map(int, input().split()))
    for i in range(n):
        if now == -1:
            if a[i] > 0:
                now = 1
                v2 = max(v2, a[i])
            else:
                now = 0
                v1 = max(v1, a[i])
        else:
            if a[i] > 0:
                if now == 0:
                    ans += v1
                    v1 = -1e9
                v2 = max(v2, a[i])
                now = 1
            else:
                if now == 1:
                    ans += v2
                    v2 = 0
                v1 = max(v1, a[i])
                now = 0
    if now == 0:
        ans += v1
    else:
        ans += v2
    print(int(ans))  # Convert ans to an integer before printing


if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        max_alternating_sum()
