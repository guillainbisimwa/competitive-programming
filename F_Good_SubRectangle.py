def calculate_prefix_sums(matrix, rows, cols):
  
  prefix_sums = [[0 for _ in range(cols)] for _ in range(rows)]  # Initialize prefix sums with zeros

  # Fill the first row and column directly from the original matrix
  prefix_sums[0][0] = matrix[0][0]
  for i in range(1, rows):
      prefix_sums[i][0] = matrix[i][0] + prefix_sums[i - 1][0]
  for j in range(1, cols):
      prefix_sums[0][j] = matrix[0][j] + prefix_sums[0][j - 1]

  for r in range(1, rows):
      for c in range(1, cols):
          prefix_sums[r][c] = matrix[r][c] + prefix_sums[r - 1][c] + prefix_sums[r][c - 1] - prefix_sums[r - 1][c - 1]

  return prefix_sums

def get_rectangle_sum(prefix_sums, top_row, left_col, bottom_row, right_col):
  

  area_sum = prefix_sums[bottom_row][right_col]  # Start with the sum of the entire rectangle

  # Adjust for overlapping areas calculated multiple times
  if top_row > 0:
      area_sum -= prefix_sums[top_row - 1][right_col]  # Subtract the sum above the rectangle
  if left_col > 0:
      area_sum -= prefix_sums[bottom_row][left_col - 1]  # Subtract the sum to the left of the rectangle
  if top_row > 0 and left_col > 0:
      area_sum += prefix_sums[top_row - 1][left_col - 1]  # Add back the sum of the overlapping corner

  return area_sum

rows, cols = map(int, input().split())
matrix = []
for _ in range(rows):
    matrix.append(list(map(int, input().split())))

prefix_sums = calculate_prefix_sums(matrix, rows, cols)

max_area = 0
for top_row in range(rows):
    for bottom_row in range(top_row, rows):
        for left_col in range(cols):
            for right_col in range(left_col, cols):
                area_sum = get_rectangle_sum(prefix_sums, top_row, left_col, bottom_row, right_col)
                area = (bottom_row - top_row + 1) * (right_col - left_col + 1)
                if 2 * area_sum == area:  # Check if sum is half of the area
                    max_area = max(max_area, area)

print(max_area)
