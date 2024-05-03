class Solution:
    def decodeString(self, s: str) -> str:
        ans = ""
        i = 0

        while i < len(s):
            val = s[i]
            ans1 = ""
            a = 0
            count = 1
            num = ""
            while s[i].isdigit():
                num += s[i]
                i += 1

            if num:
                a = int(num)
                i += 1
                while count > 0:
                    if s[i] == '[':
                        count += 1
                    if s[i] == ']':
                        count -= 1
                    if s[i] == ']' and count == 0:
                        break
                    ans1 += s[i]
                    i += 1
            else:
                ans += val

            for _ in range(a):
                ans += ans1

            i += 1

        if "[" in ans or "]" in ans:
            return self.decodeString(ans)
        return ans