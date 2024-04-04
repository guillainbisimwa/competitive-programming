class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        char_counts = {}
        max_f_count = 0
        left, right = 0, 0
        max_length = 0

        while right < len(answerKey):
            current_char = answerKey[right]
            char_counts[current_char] = char_counts.get(current_char, 0) + 1
            max_f_count = max(max_f_count, char_counts[current_char]) 

            while right - left + 1 - max_f_count > k:
                removed_char = answerKey[left]
                char_counts[removed_char] -= 1
                if char_counts[removed_char] == 0:
                    del char_counts[removed_char] 
                left += 1

            max_length = max(max_length, right - left + 1)

            right += 1

        return max_length