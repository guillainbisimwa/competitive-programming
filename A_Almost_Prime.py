from collections import defaultdict

def count_semiprimes(end):
    memo = defaultdict(int)
    total_semiprimes = 0

    for i in range(2, end + 1):
        prime_factors_count = 0
        divisor = 2
        n = i
        memo_found = False
        
        while divisor * divisor <= i:
            if n in memo: 
                prime_factors_count += memo[n]
                memo_found = True
                break
            if n % divisor == 0:
                prime_factors_count += 1
            while n % divisor == 0:
                n //= divisor
            divisor += 1
        
        if n != 1 and not memo_found:
            prime_factors_count += 1
        
        memo[i] = prime_factors_count
        
        if prime_factors_count == 2:
            total_semiprimes += 1

    return total_semiprimes

# Input and function call
end = int(input())
print(count_semiprimes(end))
