import sys
import math

def main():
    input = sys.stdin.read
    data = input().split()
    # data = list(map(int, input().split()))

    idx = 0

    t = int(data[idx])
    idx += 1
    
    results = []
    
    while t > 0:
        t -= 1
        n = int(data[idx])
        idx += 1
        
        a = [0] * (n + 1)
        f = [[math.inf] * (n + 1) for _ in range(n + 1)]
        
        for i in range(1, n + 1):
            a[int(data[idx])] += 1
            idx += 1
            
        f[0][0] = 0
        
        for i in range(1, n + 1):
            for j in range(n + 1):
                f[i][j] = math.inf
                if j + a[i] <= n:
                    f[i][j] = min(f[i][j], f[i - 1][j + a[i]])
                if j > 0:
                    f[i][j] = min(f[i][j], f[i - 1][j - 1] + 1)
        
        results.append(min(f[n][:n+1]))
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
