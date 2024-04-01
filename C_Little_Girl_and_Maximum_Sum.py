# def max_query_sum(n, q, array, queries):
#     array.sort()

#     queries.sort()

#     total_sum = 0

#     for l, r in queries:
#         total_sum += sum(array[-(r - l + 1):])

#     return total_sum

# n, q = map(int, input().split())
# array = list(map(int, input().split()))
# queries = [tuple(map(int, input().split())) for _ in range(q)]

# print(max_query_sum(n, q, array, queries))

n , q = map(int,input().split())
a = list(map(int,input().split()))
prefix_sum = [0] * (n+1)
for i in range(q):
    l,r = map(int,input().split())
    prefix_sum[l] +=1
    if r < n:
        prefix_sum[r+1] -=1
double = [0]
for i in prefix_sum:
    double.append(double[-1] + i)
a.sort(reverse=True)
double.sort(reverse=True)
total = 0
for i in range(n):
    total += a[i] * double[i]

print(total)