def find_final_entrance(n, a, b):
    
    final_entrance = (a + b - 1) % n + 1
    return final_entrance

def main():
    n, a, b = map(int, input().split())
    print(find_final_entrance(n, a, b))

if __name__ == "__main__":
    main()
