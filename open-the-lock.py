class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        
        if "0000" in deadends or target in deadends:
            return -1
        
        queue = [("0000", 0)]
        visited = set("0000")
        
        while queue:
            state, moves = queue.pop(0)
            
            if state == target:
                return moves
            
            for i in range(4):
                digit = int(state[i])
                for move in (-1, 1):
                    nextChar = (digit + move) % 10
                    next_state = state[:i] + str(nextChar) + state[i+1:]
                    
                    if next_state not in deadends and next_state not in visited:
                        visited.add(next_state)
                        queue.append((next_state, moves + 1))
        
        return -1