class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = []
        for i in tokens:
            if i not in {'+','*','-','/'}:
                res.append(int(i))
            else:
                b = res.pop()
                a = res.pop()
                if i == '+':
                    res.append(a+b)
                elif i == '-':
                    res.append(a-b)
                elif i == '*':
                    res.append(a*b)
                elif i == '/':
                    res.append(int(a/b))
        return res.pop()