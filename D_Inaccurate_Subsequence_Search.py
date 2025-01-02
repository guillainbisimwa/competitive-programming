def count_good_subarrays():
    t = int(input())
    results = []

    for _ in range(t):
        n, m, k = map(int, input().split())
        array_a = list(map(int, input().split()))
        array_b = list(map(int, input().split()))
        
        overlap_count = 0
        valid_subarrays = 0
        max_element = max(max(array_a), max(array_b)) + 1

        freq_a = [0] * max_element
        freq_b = [0] * max_element

        for index in range(m):
            freq_a[array_a[index]] += 1
            freq_b[array_b[index]] += 1

        for value in range(max_element):
            overlap_count += min(freq_a[value], freq_b[value])

        if overlap_count >= k:
            valid_subarrays += 1

        for index in range(m, n):
            if freq_a[array_a[index]] < freq_b[array_a[index]]:
                overlap_count += 1
            freq_a[array_a[index]] += 1

            if freq_a[array_a[index - m]] <= freq_b[array_a[index - m]]:
                overlap_count -= 1
            freq_a[array_a[index - m]] -= 1

            if overlap_count >= k:
                valid_subarrays += 1

        results.append(valid_subarrays)

    for result in results:
        print(result)

count_good_subarrays()
