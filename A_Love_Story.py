def count_differences(s):

    count = 0
    for i in range(10):
        if s[i] != "codeforces"[i]:
            count += 1
    return count

test = int(input()) 

for _ in range(test):
    s = input()  
    differences = count_differences(s)
    print(differences)
