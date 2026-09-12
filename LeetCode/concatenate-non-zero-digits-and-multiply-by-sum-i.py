class Solution:
    def sumAndMultiply(self, n: int) -> int:
        su = 0
        s = ''
        for i in str(n):
            if i != '0':
                s += i
                su += ord(i) - ord('0')
        return int(s)*su if len(s) != 0 else 0