s = input()
stack = []

i = 0

while i < len(s):
    if s[i] == "<":
        if stack:
            stack.pop()
        i +=2
    else:
        stack.append(s[i])
        i += 1

print("".join(stack))