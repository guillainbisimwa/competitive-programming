def search(v, s):
    i, j = -1, -1
    j = s.rfind(v[1])
    if j != -1:
        i = s.rfind(v[0], 0, j - 1)
    k = s.rfind(v)
    return max(i, k)

def main():
    val = ["00", "25", "50", "75"]
    t = int(input())
    
    while t > 0:
        s = input()
        max_val = float('-inf')
        
        if int(s) % 25 == 0:
            print("0")
            t -= 1
            continue

        for v in val:
            i = search(v, s)
            if i > max_val:
                max_val = i
        
        print(len(s) - max_val - 2)
        t -= 1

if __name__ == "__main__":
    main()
