def main():
    a = int(input())
    
    arr = list(map(int, input().split()))

    count = 1
    cnt = 1
    
    for i in range(1, a):
        if arr[i] > arr[i - 1]:
            cnt += 1
        else:
            if cnt > count:
                count = cnt
            cnt = 1
    
    # Update the maxi
    if cnt > count:
        count = cnt    
    print(count)
main()
