class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        lbl = 1
        cells = [(0, 0)] * (n * n + 1)
        columns = list(range(n))
        
        for row in range(n - 1, -1, -1):
            for column in columns:
                cells[lbl] = (row, column)
                lbl += 1
            columns.reverse()
        
        dist = [-1] * (n * n + 1)
        dist[1] = 0
        q = deque([1])
        
        while q:
            curr = q.popleft()
            for next_cell in range(curr + 1, min(curr + 6, n * n) + 1):
                row, column = cells[next_cell]
                destination = board[row][column] if board[row][column] != -1 else next_cell
                if dist[destination] == -1:
                    dist[destination] = dist[curr] + 1
                    q.append(destination)
        
        return dist[n * n]