def hermosa(n): 
    gauche, droite, cnt = n * n, 1, 0
    ans = [[0] * n for _ in range(n)]
    for i in range(n):
        if not (i & 1):
            for j in range(n):
                cnt += 1
                if cnt & 1:
                    ans[i][j] = gauche
                    gauche -= 1
                else:
                    ans[i][j] = droite
                    droite += 1
        else:
            for j in range(n - 1, -1, -1):
                cnt += 1
                if cnt & 1:
                    ans[i][j] = gauche
                    gauche -= 1
                else:
                    ans[i][j] = droite
                    droite += 1
    for i in ans:
        print(*i)


if __name__ == "__main__":
    n = int(input())
    x = list(map(int, input().split()))
    hermosa(n)