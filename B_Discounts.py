# Input
n = int(input()) 
prices = list(map(int, input().split()))
m = int(input()) 
coupons = list(map(int, input().split())) 

prices.sort(reverse=True)

total_cost = sum(prices)

for q in coupons:
    discount = prices[q - 1]
    min_cost = total_cost - discount
    print(min_cost)
