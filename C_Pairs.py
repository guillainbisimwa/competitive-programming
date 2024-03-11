
# def count_pairs(N, a, b, c):
#     # Create a dictionary to count occurrences of elements in array c
#     count_c = {}
#     for ci in c:
#         count_c[ci] = count_c.get(ci, 0) + 1
    
#     # Initialize the total count of pairs
#     total_pairs = 0
    
#     # Iterate through each element ai in array a
#     for ai in a:
#         # Calculate how many elements in array b match with ai*ci for each distinct ci in array c
#         for ci, count in count_c.items():
#             bi = ai * ci
#             if bi in b:
#                 total_pairs += count * b.count(bi)
    
#     return total_pairs

# # Input
# N = int(input())
# a = list(map(int, input().split()))
# b = list(map(int, input().split()))
# c = list(map(int, input().split()))

# # Output
# print(count_pairs(N, a, b, c))
