class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
       
        rows, cols = len(matrix), len(matrix[0])
        count = 0

        # Precompute cumulative sums for efficient submatrix sum calculations
        cumulative_sum = [[0] * (cols + 1) for _ in range(rows + 1)]
        for r in range(rows):
            for c in range(cols):
                cumulative_sum[r + 1][c + 1] = (
                    cumulative_sum[r + 1][c]
                    + cumulative_sum[r][c + 1]
                    - cumulative_sum[r][c]
                    + matrix[r][c]
                )

        # Find submatrices with the target sum using cumulative sums and a hash map
        for r1 in range(1, rows + 1):
            for r2 in range(r1, rows + 1):
                sum_count = {0: 1}  # Initialize with count 1 for empty submatrix with sum 0
                current_sum = 0
                for c in range(1, cols + 1):
                    current_sum = cumulative_sum[r2][c] - cumulative_sum[r1 - 1][c]
                    # Check if a previous submatrix ending at this column has a sum that
                    # combined with the current sum, equals the target
                    count += sum_count.get(current_sum - target, 0)
                    # Update count for the current cumulative sum
                    sum_count[current_sum] = sum_count.get(current_sum, 0) + 1

        return count
