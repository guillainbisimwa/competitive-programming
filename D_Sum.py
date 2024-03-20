def calculate_maximum_sum(size, k, arr):
    maximum = 0
    preSum = [0] * (size + 1)

    # Calculate prefix sum
    for i in range(size):
        preSum[i + 1] = preSum[i] + arr[i]

    # Iterate over possible values of i
    for i in range(k + 1):
        maximum = max(maximum, (preSum[size - (k - i)] - preSum[i * 2]))

    return maximum

def main():
    test = int(input())
    for _ in range(test):
        size, k = map(int, input().split())
        arr = sorted(list(map(int, input().split())))

        maximum = calculate_maximum_sum(size, k, arr)
        print(maximum)

if __name__ == "__main__":
    main()
