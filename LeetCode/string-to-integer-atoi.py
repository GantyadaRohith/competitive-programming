class Solution:
    def myAtoi(self, s: str) -> int:
        x = s.strip()
        if len(x) == 0:
            return 0
        sign = 1
        if x[0] == '-':
            sign = -1
            x=x[1:]
        elif x[0] == '+':
            x = x[1:]
        num = 0
        for i in x:
            if i.isdigit():
                num = num*10 + int(i)
            else:
                break
        if num*sign > 2**31 -1:
            return 2**31 - 1
        elif num*sign < 2**31 * -1:
            return 2**31*-1
        else:
            return num*sign 
            