 
def main():
    t = int(input())
    for _ in range(t):
        x, y = map(int, input().split())
        print(min(x, y), max(x, y))
 
if __name__ == "__main__":
    main()