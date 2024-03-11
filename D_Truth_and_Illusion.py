# def min_operations(grid):
#     """
#     Calculates the minimum number of operations to make the grid rotationally symmetric.

#     Args:
#         grid: A list of lists representing the grid (n x n matrix).

#     Returns:
#         The minimum number of operations required.
#     """
#     n = len(grid)

#     # Check differences between corresponding cells in the grid and its transpose
#     operations = 0
#     for i in range(n):
#         for j in range(i, n):
#             if grid[i][j] != grid[j][i]:
#                 operations += 1

#     # Check differences between top-left and bottom-right diagonals
#     for i in range(n):
#         if grid[i][i] != grid[n - 1 - i][n - 1 - i]:
#             operations += 1

#     return operations

# def main():
#     """
#     Reads input, calculates minimum operations for each test case, and prints results.
#     """
#     t = int(input())
#     for _ in range(t):
#         n = int(input())
#         grid = [input() for _ in range(n)]
#         grid = [list(map(int, row)) for row in grid]  # Convert string input to integers
#         min_ops = min_operations(grid)
#         print(min_ops)

# if __name__ == "__main__":
#     main()
