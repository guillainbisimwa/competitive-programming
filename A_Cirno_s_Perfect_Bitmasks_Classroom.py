def find_answer(m):
    for i in range(m.bit_length()): 
        if m & (1 << i) != 0:
            break
    ans = 1 << i
    
    if m == 1:
        return 3
    elif m == ans:
        return ans + 1
    else:
        return ans

def start():
    t = int(input())
    for _ in range(t):
        m = int(input())
        print(find_answer(m))

start()
