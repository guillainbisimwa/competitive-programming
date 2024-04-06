class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for char in s:
            if char == '(':
                stack.append('')
            elif char == ')':
                substring = stack.pop()[::-1]
                if stack:
                    stack[-1] += substring
                else:
                    stack.append(substring)
            else:
                if stack:
                    stack[-1] += char
                else:
                    stack.append(char)
        return ''.join(stack)
