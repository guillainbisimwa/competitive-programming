import math

def generate_primes(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0], is_prime[1] = False, False
    for i in range(2, int(math.sqrt(limit)) + 1):
        if is_prime[i]:
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False
    return {i for i, prime in enumerate(is_prime) if prime}  

def is_t_prime(x, primes_set):
    root = int(math.isqrt(x))
    return root * root == x and root in primes_set

def main():
    n = int(input().strip())
    numbers = list(map(int, input().split()))

    limit = int(10**6)
    primes_set = generate_primes(limit)

    result = []
    for number in numbers:
        if is_t_prime(number, primes_set):
            result.append("YES")
        else:
            result.append("NO")

    print("\n".join(result))
