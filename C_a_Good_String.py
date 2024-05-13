def need_to_change(c, st, sp, s):
    cnt = 0
    for i in range(st, sp + 1):
        if s[i] != c:
            cnt += 1
    return cnt

def cal(c, st, sp, s):
    if st == sp:
        return 0 if s[st] == c else 1

    mid = (st + sp) // 2
    return min(need_to_change(c, st, mid, s) + cal(chr(ord(c) + 1), mid + 1, sp, s), need_to_change(c, mid + 1, sp, s) + cal(chr(ord(c) + 1), st, mid, s))

nums = int(input())
for _ in range(nums):
    n = int(input())
    s = input().strip()

    st, sp = 0, n - 1

    print(cal('a', st, sp, s))