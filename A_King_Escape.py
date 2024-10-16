def can_queen_reach_goal():
    num_moves = int(input())
    queen_x, queen_y = map(int, input().split())
    knight_x, knight_y = map(int, input().split())
    goal_x, goal_y = map(int, input().split())

    if (knight_x <= queen_x <= goal_x or knight_x >= queen_x >= goal_x or
        knight_y <= queen_y <= goal_y or knight_y >= queen_y >= goal_y):
        print('NO')
        return

    diagonal_queen = queen_x - queen_y
    anti_diagonal_queen = queen_x + queen_y

    if (knight_x + knight_y <= diagonal_queen <= goal_x + goal_y or
        knight_x + knight_y <= anti_diagonal_queen <= goal_x - goal_y):
        print('NO')
    else:
        print('YES')


can_queen_reach_goal()
