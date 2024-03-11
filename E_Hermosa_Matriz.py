# def create_beautiful_matrix(n):
#   matrix = [[0 for _ in range(n)] for _ in range(n)]

#   # Base case: n = 2
#   if n == 2:
#     return [[1, 2], [4, 3]]

#   # Calculate the offset for alternating increments/decrements
#   offset = (n - 3) // 4

#   # Fill the diagonal and the top row (except the last element)
#   mid = (n + 1) // 2
#   for i in range(n):
#     matrix[i][i] = mid + i if i < n // 2 else mid - (i - n // 2)
#     if i < n - 1:
#       matrix[0][i] = n * n - i

#   # Fill the bottom row (except the last element) and the last column
#   for i in range(1, n):
#     matrix[n - 1][i] = matrix[0][i - 1] - n + 1
#     if i < n - 1:
#       matrix[i][n - 1] = matrix[i - 1][0] + n - 1

#   # Fill the remaining elements in the top and bottom rows with alternating increments/decrements
#   value = n * n
#   for i in range(n - 1, 0, -1):
#     matrix[0][i - 1] = value
#     matrix[n - 1][i] = value - (2 * offset + 1)
#     value -= 2

#   return matrix

# def main():
#   """
#   Reads input, generates beautiful matrices for each test case, and prints results.
#   """
#   t = int(input())
#   for _ in range(t):
#     n = int(input())
#     beautiful_matrix = create_beautiful_matrix(n)
#     for row in beautiful_matrix:
#       print(*row)  # Print each row of the matrix

# if __name__ == "__main__":
#   main()
