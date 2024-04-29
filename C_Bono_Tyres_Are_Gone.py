n = 2 * int(input())

stack = []
ans = 0
num = 1

for _ in range(n):
    command = input()

    if command[0] == 'r':
        if stack and stack[-1] == num:
            stack.pop()
        elif stack  and stack[-1] != num:
            ans += 1
            stack = []
        num += 1
    else:
        number = int(command.split()[1])
        stack.append(number)
print(ans)
