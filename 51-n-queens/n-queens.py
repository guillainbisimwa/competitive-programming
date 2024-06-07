class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        def backtracking(row: int):
            if row == n:
                # If we have placed queens in all rows, we have found a solution
                board = []
                for i in range(n):
                    board.append("".join(chess[i]))
                solutions.append(board)
                return
            
            for col in range(n):
                if is_valid(row, col):
                    # Apply choice
                    chess[row][col] = 'Q'
                    columns.add(col)
                    posDiag.add(row - col)
                    negDiag.add(row + col)
                    
                    # Find solution
                    backtracking(row + 1)
                    
                    # Remove choice
                    chess[row][col] = '.'
                    columns.remove(col)
                    posDiag.remove(row - col)
                    negDiag.remove(row + col)
        
        def is_valid(row: int, col: int) -> bool:
            return col not in columns and (row - col) not in posDiag and (row + col) not in negDiag

        # Initialize variables
        solutions = []
        chess = [['.' for _ in range(n)] for _ in range(n)]
        columns = set()
        posDiag = set()
        negDiag = set()
        
        # Start backtracking from the first row
        backtracking(0)
        
        return solutions