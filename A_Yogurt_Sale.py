# Function to calculate the minimum cost of buying yogurts
def min(t, res):
    for i in range(t):
        n, a, b = res[i]

        if b <= 2 * a:
            min_cost = (n // 2) * b + (n % 2) * a
        else:
            min_cost = n * a

        print(min_cost)

t = int(input())
res = [] 
for _ in range(t):
    n, a, b = map(int, input().split()) 
    res.append((n, a, b)) 

min(t, res)
