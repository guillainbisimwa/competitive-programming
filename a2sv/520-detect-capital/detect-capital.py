class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        all_upper = True
        all_lower = True
        title_case = True

        for i in range(len(word)):
            if 'A' <= word[i] <= 'Z':
                all_lower = False
                if i > 0:
                    title_case = False
            elif 'a' <= word[i] <= 'z':
                all_upper = False
                if i == 0:
                    title_case = False
            else:
                return False

        return all_upper or all_lower or title_case
