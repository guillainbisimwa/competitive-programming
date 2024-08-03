def say(n):
    word = 'hello'

    current = 0
    out = 'NO'
    for i in n:
        if i == word[current]:
            current += 1
        if current == 5:
            out = 'YES'
            break
    print(out)

n = input()
say(n)
