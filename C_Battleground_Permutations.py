def calculate_permutations(arr1, arr2):
    modulo = 10 ** 9 + 7
    ans = 1
    j = 0
    t = len(arr1)
    
    for i in range(t):
        while j < t and arr2[j] < arr1[i]:
            j += 1
        ans *= (j - i)
        ans %= modulo
    
    return ans

def main():
    n = int(input())
    for _ in range(n):
        t = int(input())
        arr1 = list(map(int, input().split()))
        arr2 = list(map(int, input().split()))

        arr1.sort()
        arr2.sort()

        ans = calculate_permutations(arr1, arr2)
        print(ans)

if __name__ == "__main__":
    main()
