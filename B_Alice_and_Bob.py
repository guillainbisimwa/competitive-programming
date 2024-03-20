test_cases = int(input())

for _ in range(test_cases):
    a, b, k = map(int, input().split())
    str_a = sorted(input())
    str_b = sorted(input())
    ans = ""
    ind_a, ind_b = 0, 0
    count_a, count_b = 0, 0
    
    while ind_a < a and ind_b < b:
        if str_a[ind_a] < str_b[ind_b] and count_a < k:
            ans += str_a[ind_a]
            count_a += 1
            count_b = 0
            ind_a += 1
        elif str_a[ind_a] > str_b[ind_b] and count_b < k:
            ans += str_b[ind_b]
            count_b += 1
            count_a = 0
            ind_b += 1
        else:
            if count_a < k:
                ans += str_a[ind_a]
                count_a += 1
                count_b = 0
                ind_a += 1
            else:
                ans += str_b[ind_b]
                count_b += 1
                count_a = 0
                ind_b += 1
                
    print(ans)
