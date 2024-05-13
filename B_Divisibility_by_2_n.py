
def is_power_of_two(num):
    while num > 1:
        if num % 2 != 0:
            return False
        num //= 2
    return True

def generate_powers_of_two(upper_limit):
    powers_of_two = []
    for i in range(1, upper_limit + 1):
        if is_power_of_two(i):
            powers_of_two.append(i)
    return powers_of_two

def findNumberOfOps(need, nums, n):
    ops = [0] * n

    for i in range(n, 0, -1):
        num = i
        while num % 2 == 0:
            num //= 2
            ops[i - 1] += 1
    
    ops.sort(reverse=True)
    ans = totSum = 0 
    for i, op in enumerate(ops):
        totSum += op 
        if totSum >= need:
            return i + 1 
    return -1
    
def main():
    for _ in range(int(input())):
        n = int(input())
        nums = list(map(int, input().split()))

        powers = 0 
        for num in nums:
            while num % 2 == 0:
                powers += 1
                num //= 2
        
        need = n - powers
        if need > 0:
            print(findNumberOfOps(need, nums, n))
        else:
            print(0)

if __name__ == "__main__":
    main()
