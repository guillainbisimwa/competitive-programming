import math

def process_test_case(length, array):
  
    adjustments = 0  # Track the number of adjustments needed
    for idx in range(length - 2, -1, -1):
        if array[idx] > array[idx + 1]:
            scaling_factor = math.ceil(array[idx] / array[idx + 1])
            adjustments += scaling_factor - 1
            array[idx] //= scaling_factor
    return adjustments

def main():

    num_tests = int(input())
    results = []
    for _ in range(num_tests):
        arr_length = int(input())
        arr = list(map(int, input().split()))
        results.append(process_test_case(arr_length, arr))
    
    # Output all results
    for result in results:
        print(result)

if __name__ == "__main__":
    main()

