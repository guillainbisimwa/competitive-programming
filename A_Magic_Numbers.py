# def magicNumber(n):
#     magic = [(i) for i in str(n)]
#     print(magic)

#     def bactracking():
#         # if condition


#         # loop through all choices

#         # if good choise found

#         # remove choise
#         pass

#     pass

# n = int(input())
# magicNumber(n)
def magicNumber(n):
    magic_nums = [1, 14, 144]

    def backtracking(index):
        if index == len(str(n)):
            return True

        for magic_num in magic_nums:
            magic_str = str(magic_num)
            if int(str(n)[index:index + len(magic_str)]) == magic_num:
                if backtracking(index + len(magic_str)):
                    return True

        return False

    if backtracking(0):
        print("YES")
    else:
        print("NO")

n = int(input())
magicNumber(n)


