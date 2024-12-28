class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        n, m = len(grid), len(grid[0])  # Grid dimensions
        total_keys = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Directions for movement
        visited = set()  # To track visited states
        queue = deque()  # BFS queue
        
        # Initialize the BFS queue and count the total keys
        for i in range(n):
            for j in range(m):
                if 'a' <= grid[i][j] <= 'z':
                    total_keys += 1
                if grid[i][j] == '@':
                    queue.append((i, j, 0, 0))  # (x, y, mask, steps)

        # Perform BFS
        while queue:
            x, y, mask, steps = queue.popleft()
            
            # Check if all keys are collected
            if bin(mask).count('1') == total_keys:
                return steps

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                
                # Validate the new position
                if not (0 <= nx < n and 0 <= ny < m) or grid[nx][ny] == '#':
                    continue
                
                new_mask = mask
                cell = grid[nx][ny]

                # If it's a key, add it to the mask
                if 'a' <= cell <= 'z':
                    new_mask |= (1 << (ord(cell) - ord('a')))
                
                # If it's a lock, check if the key is available
                if 'A' <= cell <= 'Z' and not (mask & (1 << (ord(cell) - ord('A')))):
                    continue
                
                # Check if the new state is already visited
                if (nx, ny, new_mask) in visited:
                    continue

                visited.add((nx, ny, new_mask))
                queue.append((nx, ny, new_mask, steps + 1))
        
        return -1