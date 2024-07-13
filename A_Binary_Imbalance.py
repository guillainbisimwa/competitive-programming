
# def chars(n):
#     while n > 0:
#         s = input()
#         s = input()
#         count = {}
#         for char in s:
#             if char in count:
#                 count[char] += 1
#             else:
#                 count[char] = 1
        
#         if len(count) == 1 and s[0] == '1':
#             print('NO')
#         else:
#             print('YES')
#         n -= 1
# n = int(input())
# chars(n)
import heapq

def top_k(words, k):
    counter = {}
    for word in words:
        if word in counter:
            counter[word] += 1
        else:
            counter[word] = 1

    heap = []
    for word, count in counter.items():
        heapq.heappush(heap, (-count, word))

    result = []
    for _ in range(k):
        count, word = heapq.heappop(heap)
        result.append(word)

    return result

i = int(input())
while i > 0:
    n = int(input())
    s = input()
    words = list(s)
    
    k = 1
    frequent_words = top_k(words, k)
    
    if len(frequent_words) == 1 and frequent_words[0] == '1':
        print('NO')
    else:
        print('YES')
    
    i -= 1
