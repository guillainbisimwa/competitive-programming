def count_substring(string, substring):


  count = 0
  for i in range(len(string) - len(substring) + 1):
    # Check if the substring matches the current window in the string
    if string[i:i + len(substring)] == substring:
      count += 1

  return count

string = input("Enter the original string: ")
substring = input("Enter the substring: ")

occurrences = count_substring(string, substring)

print(f"The substring '{substring}' appears {occurrences} times in '{string}'.")
