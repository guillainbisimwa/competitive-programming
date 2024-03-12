word = "ABCDIEFG"
print(len(word) // 2)

for i in range(len(word) // 2):
    print(word[i])
    print(word[-(i + 1)])
    print()