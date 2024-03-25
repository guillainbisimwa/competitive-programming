import sys
 
def find_longest_sequence(n, x):
    ans = 1
    for i in range(n):
        cnt = 0
        for j in range(i, min(i + 26, n)):
            if j - i == ord(x[j]) - ord(x[i]):
                cnt += 1
            else:
                break
        ans = max(ans, cnt)
    return ans
 
n = int(sys.stdin.readline().strip())
x = sys.stdin.readline().strip()
print(find_longest_sequence(n, x))