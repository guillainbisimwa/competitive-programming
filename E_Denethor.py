# def min_deployed_commanders(first_list, last_list):
#   """
#   This function finds the minimum number of commanders deployed between two lists.

#   Args:
#       first_list: A list of integers representing commander IDs at the beginning.
#       last_list: A list of integers representing commander IDs at the end.

#   Returns:
#       An integer representing the minimum number of deployed commanders.
#   """
#   # Initialize variables for tracking differences
#   i, j, deployed = 0, 0, 0

#   # Iterate through both lists simultaneously
#   while i < len(first_list) and j < len(last_list):
#     # Check if commanders match in both lists (not deployed)
#     if first_list[i] == last_list[j]:
#       i += 1
#       j += 1
#     # If commanders differ in first list, they were deployed
#     elif first_list[i] > last_list[j]:
#       deployed += 1
#       i += 1
#     # If commanders differ in last list, check if remaining first list elements match any later elements
#     else:
#       # Look for a match for the remaining commanders in the first list (avoid overcounting)
#       found_match = False
#       for k in range(j, len(last_list)):
#         if first_list[i] == last_list[k]:
#           found_match = True
#           break
#       if not found_match:
#         deployed += 1
#       i += 1
#       j += 1

#   return deployed


# def main():
#   # Get the number of test cases
#   num_tests = int(input())

#   for _ in range(num_tests):
#     # Get the number of commanders
#     n = int(input())

#     # Get the commander list at the beginning of the month
#     first_list = list(map(int, input().split()))

#     # Get the commander list at the end of the month
#     last_list = list(map(int, input().split()))

#     # Find and print the minimum number of deployed commanders
#     min_deployed = min_deployed_commanders(first_list, last_list)
#     print(min_deployed)

# if __name__ == "__main__":
#   main()
