INF = 100
 
def solve(s, t):
    sptr = len(s) - 1
    ans = 0
 
    while sptr >= 0 and s[sptr] != t[1]:
        sptr -= 1
        ans += 1
 
    if sptr < 0:
        return INF
 
    sptr -= 1
 
    while sptr >= 0 and s[sptr] != t[0]:
        sptr -= 1
        ans += 1
 
    return INF if sptr < 0 else ans
 
def main():
    t = int(input())
 
    for _ in range(t):
        n = input()
        ans = INF
 
        for e in ["00", "25", "50", "75"]:
            ans = min(ans, solve(n, e))
 
        print(ans)
 
if __name__ == "__main__":
    main()