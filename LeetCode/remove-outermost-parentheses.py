class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res = ''
        op = 0
        for i in range(len(s)):
            if s[i] == '(':
                if op > 0:
                    res = res + s[i]
                op+=1
            elif s[i] == ')':
                op-=1
                if op>0:
                    res = res + s[i]
        return res