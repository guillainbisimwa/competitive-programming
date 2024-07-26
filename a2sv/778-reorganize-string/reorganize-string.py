class Solution:
    def reorganizeString(self, s: str) -> str:
        freq_map = {}
        for char in s:
            if char in freq_map:
                freq_map[char] += 1
            else:
                freq_map[char] = 1
        
        sorted_chars = sorted(freq_map.keys(), key=lambda x: freq_map[x], reverse=True)
        
        if freq_map[sorted_chars[0]] > (len(s) + 1) // 2:
            return ""
        
        result = [""] * len(s)
        
        index = 0
        for char in sorted_chars:
            count = freq_map[char]
            for _ in range(count):
                if index >= len(s):
                    index = 1
                result[index] = char
                index += 2
        
        final_result = ""
        for char in result:
            final_result += char
        
        return final_result
