def minimum_deux(n, x):
    x = sorted(x)
 
    print(1, x[0])
    x.pop(0)
 
    if x[-1] > 0:
        print(1, x[-1])
        x.pop(-1)
    else:
        print(2, x[0], x[1])
        x.pop(0)
        x.pop(0)
 
    print(len(x), *x)
 
if __name__ == "__main__":
    n = int(input())
    x = list(map(int, input().split()))
    minimum_deux(n, x)