# t = int(input())
# while t:
#     s = input()
#     cuts = 0
#     join = 0
#     for i in range(len(s) - 1):
#         cuts += s[i] != s[i + 1]
#         if s[i] == "0" and s[i + 1] == "1":
#             join = 1
#     print(cuts + 1 - join)
#     t -= 1

def process_string(s):
    cuts = 0
    join = 0
    for i in range(len(s) - 1):
        cuts += s[i] != s[i + 1]
        if s[i] == "0" and s[i + 1] == "1":
            join = 1
    return cuts + 1 - join

def main():
    t = int(input())
    results = []
    while t:
        s = input()
        result = process_string(s)
        results.append(result)
        t -= 1
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()