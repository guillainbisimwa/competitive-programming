# def max_difference(frodo_list, sam_list):
#   """
#   This function finds the maximum difference between two lists of integers.

#   Args:
#       frodo_list: A list of integers representing Frodo's list.
#       sam_list: A list of integers representing Sam's potential list.

#   Returns:
#       An integer representing the maximum total difference achievable by Sam.
#   """
#   # Sort Sam's list in descending order (maximize difference)
#   sam_list.sort(reverse=True)

#   total_diff = 0
#   # Iterate through Frodo's list (shorter list)
#   for i in range(len(frodo_list)):
#     # Get the absolute difference between corresponding elements
#     diff = abs(frodo_list[i] - sam_list[i])
#     # Accumulate the difference
#     total_diff += diff

#   return total_diff

# def main():
#   # Get the number of test cases
#   num_tests = int(input())

#   for _ in range(num_tests):
#     # Get n (number of elements in Frodo's list) and m (number of elements in Sam's list)
#     n, m = map(int, input().split())

#     # Get Frodo's list
#     frodo_list = list(map(int, input().split()))

#     # Get Sam's list
#     sam_list = list(map(int, input().split()))

#     # Find and print the maximum difference Sam can achieve
#     max_diff = max_difference(frodo_list, sam_list)
#     print(max_diff)

# if __name__ == "__main__":
#   main()
