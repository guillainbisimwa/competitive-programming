# 

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
        x = int(data[index + 1])
        index += 2

        a = [0] * (n + 1)
        q = -1

        for i in range(1, n + 1):
            a[i] = int(data[index])
            if a[i] == x:
                q = i
            index += 1

        l, r = 1, n + 1

        while r - l != 1:
            m = (r + l) // 2
            if a[m] <= x:
                l = m
            else:
                r = m

        if a[l] == x:
            results.append("0")
        else:
            results.append(f"1\n{l} {q}")

    print("\n".join(results))

if __name__ == "__main__":
    main()