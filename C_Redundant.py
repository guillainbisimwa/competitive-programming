def longest_repeated_substring_length(s):
    n = len(s)
    
    def has_repeated_substring(length):
        seen = set()
        for i in range(n - length + 1):
            substring = s[i:i + length]
            if substring in seen:
                return True
            seen.add(substring)
        return False

    left, right = 0, n
    result = 0
    while left <= right:
        mid = (left + right) // 2
        if has_repeated_substring(mid):
            result = mid
            left = mid + 1
        else:
            right = mid - 1

    return result

def main():
    s = input().strip()
    print(longest_repeated_substring_length(s))

if __name__ == "__main__":
    main()
