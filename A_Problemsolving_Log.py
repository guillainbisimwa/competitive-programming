def solved_problems(contest_log, duration):
    quant = [0] * 26
    solved = 0

    for i in range(duration):
        quant[ord(contest_log[i]) - ord('A')] += 1

    for i in range(26):
        if quant[i] > i:
            solved += 1
    return solved

t = int(input())
for _ in range(t):
    n = int(input())
    contest_log = input().strip()
    solved = solved_problems(contest_log, n)
    print(solved)
