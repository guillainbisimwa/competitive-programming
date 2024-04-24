class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        st = []
        for ch in s:
            if ch == '(':
                st.append("(")
            else:
                temp = 0
                while st[-1] != "(":
                    temp += int(st.pop())
                st.pop()
                if temp == 0:
                    st.append("1")
                else:
                    st.append(str(2 * temp))
        
        ans = 0
        while st:
            ans += int(st.pop())
        
        return ans