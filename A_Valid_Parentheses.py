import heapq

def validParentheses(s):
    begin = []
    end = []
    maxLen = 0

    for i in range(len(s)):
        if s[i] == '(':
            heapq.heappush(begin, i)
        else:
            if begin:
                heapq.heappop(begin)
                maxLen += 2
            else:
                heapq.heappush(end, i)
    
    return maxLen
s = input().strip()
print(validParentheses(s))
