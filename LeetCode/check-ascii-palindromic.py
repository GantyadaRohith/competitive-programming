class Solution:
    def isPalindromic(self, s: str) -> bool:
        out = []
        for i in s:
            out.append(f"{ord(i):08b}")
        s = ''.join(out)
        print(s)
        return True if s == s[::-1] else False