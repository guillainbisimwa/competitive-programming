class Solution:
    def convert(self, s: str, numRows: int) -> str:
        str_ans = ''
        if numRows == 1:
            return s
        i = 0
        while i < len(s):
            str_ans += s[i]
            i += numRows*2 -2
        for j in range(1, numRows-1):
            i = j 
            while i < len(s):
                str_ans += s[i]
                if i+(numRows*2 - (j+1)*2) < len(s):                    
                    str_ans += s[i+(numRows * 2 - (j+1) * 2 )]
                i += numRows*2 - 2     
        i = numRows - 1
        while i < len(s):
            str_ans += s[i]
            i += numRows*2 -2
        return str_ans