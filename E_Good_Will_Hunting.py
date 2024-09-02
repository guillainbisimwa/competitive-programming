l, r = map(int, input().split())
max_len = r.bit_length()

ans = l ^ r
for j in range(max_len):
    if l <= (1 << j) ^ r <= r or l <= ( 1<<j ) ^ l <= r:
        ans |= (1 << j)
print(ans)