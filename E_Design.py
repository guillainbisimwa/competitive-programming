def find_word_index(words, pref_value, suff):
  n = len(words)
  for i in range(n):
    word = words[i]
    if word.startswith(pref_value) and word.endswith(suff):
      return i 
  return -1


n, q = map(int, input().split())
words = input().split()
for _ in range(q):
    pref_value, suff = input().split()
    index = find_word_index(words, pref_value, suff)
    print(index)


