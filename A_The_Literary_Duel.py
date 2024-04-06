def final_scores(n, powers):
    hermione_score = 0
    harry_score = 0
    left = 0
    right = n - 1

    while left <= right:
        if powers[left] > powers[right]:
            hermione_score += powers[left]
            left += 1
        else:
            hermione_score += powers[right]
            right -= 1

        if left <= right:
            if powers[left] > powers[right]:
                harry_score += powers[left]
                left += 1
            else:
                harry_score += powers[right]
                right -= 1

    return hermione_score, harry_score


n = int(input())
powers = list(map(int, input().split()))

hermione_score, harry_score = final_scores(n, powers)

print(hermione_score, harry_score)
