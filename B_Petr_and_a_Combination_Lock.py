def can_point_zero(n, rotations):
    def backtracking(index, total_angle):
        if index == n:
            return total_angle % 360 == 0
        
        # Try adding the current rotation
        if backtracking(index + 1, total_angle + rotations[index]):
            return True
        
        # Try subtracting the current rotation
        if backtracking(index + 1, total_angle - rotations[index]):
            return True
        
        return False

    if backtracking(0, 0):
        return "YES"
    else:
        return "NO"

# Reading input
n = int(input())
rotations = [int(input()) for _ in range(n)]

# Checking if it's possible to point zero after rotations
print(can_point_zero(n, rotations))
