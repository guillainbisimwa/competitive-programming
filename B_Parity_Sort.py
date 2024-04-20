def parity(n, list):
    list2 = sorted(list)

    for i in range(n):
        if list[i] % 2 == list2[i] % 2:
            continue
        else:
            print("NO")
            return

    print("YES")

t = int(input())
for i in range(t):
    n = int(input())
    liste = list(map(int, input().split()))
    parity(n, liste)
