class Solution:
    def smallestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        mid = (len(s)//2)-1
        a = sorted(s[:mid+1])
        res = ''
        if len(s)&1:
            rev = a[::-1]
            res = ''.join(a) + s[mid+1] + ''.join(a[::-1])
        else:
            res = ''.join(a+a[::-1])
        return res