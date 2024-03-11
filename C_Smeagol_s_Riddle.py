def changes_min(word):

  changes = 0
  for i in range(len(word) // 2):
    if word[i] != word[-(i + 1)]:
      changes += 1

  return changes

num_words = int(input())

for _ in range(num_words):
  word = input()
  print(changes_min(word))  

  # O(N)
  # O(1)
