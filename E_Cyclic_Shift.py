# def shift(tabl_row, row, col):

#     # slide windows

#     new_tab = tabl_row * 3
#     for i in range(row):
#         tab = new_tab[i]+new_tab[i+3]+new_tab[i+6]
#         print(tab)

#     # two pointers

#     # return the minimum number of moves needed to get only numbers 1
#     pass

# #  Two space-separated integers
# row, col = map(int, input().split())

# tabl_row = [0] * row

# for i in range(row):
#     tabl_row[i] = input()

# shift(tabl_row, row, col)

def calc_cost(row):
    length = len(row)
    row = 3 * row
    left = right = length
    cost = [0] * length
    while row[left] != '1': 
        left -= 1
    for i in range (length, 2* length): 
        while right < i or row[right] != '1': 
            right += 1
        if (row[i] == '1'): 
            left = i
        cost[i - length] = min(i - left, right - i)
    return cost

def solve():
    n, m = map(int, input().split())

    mat = [0] * n
    for i in range(n):
        mat [i] = input()
    cost = [[0]* m for _ in range(n)]
    for i in range(n):
        if mat[i].count('0') ==m: 
            print(-1)
            return
        
        cost[i] = calc_cost(mat[i])

    result = float('inf')

    for col in range(m): 
        length = 0
        for row in range(n):
            length += cost[row][col]
        result = min(result, length)
    print(result)


if __name__ == "__main__":
    solve()