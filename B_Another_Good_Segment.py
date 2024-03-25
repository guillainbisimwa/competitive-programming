def b_count_subarrays(n, s, x):
    number, ans, single = 0, 0, 0
    counter =  {} 
    for i in range(n):
        while number < n and single + (counter.get(x[number], 0) == 0) <= s:
            single += (counter.get(x[number], 0) == 0)
            counter[x[number]] = counter.get(x[number], 0) + 1
            number += 1
        ans += number - i
        single -= (counter.get(x[i], 0) == 1)
        counter[x[i]] = counter.get(x[i], 0) - 1
    return ans

n, s = map(int, input().split())
x = tuple(map(int, input().split()))
print(b_count_subarrays(n, s, x))
