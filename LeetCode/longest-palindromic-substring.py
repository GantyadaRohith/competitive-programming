class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s==s[::-1]:
            return s
        start, max_len = 0, 1
        def expand(left, right):
            nonlocal start, max_len
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > max_len:
                    max_len = right - left + 1
                    start = left
                left -= 1
                right += 1
        for i in range(len(s)):
            expand(i, i)
            expand(i, i + 1)
        return s[start:start + max_len]