def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def count_burst_sequences(m, balloons):
    unique_colors = set(balloons)
    return factorial(len(unique_colors))

m = int(input())
balloons = list(map(int, input().split()))
print(count_burst_sequences(m, balloons))
