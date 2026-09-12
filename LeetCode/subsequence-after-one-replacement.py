class Solution:
    def canMakeSubsequence(self, s: str, t: str) -> bool:
        m,n = len(s),len(t)
        if m > n:
            return False
        i,j = 0,0
        for ch in t:
            if s[i] == ch:
                i+=1
            i = max(i,j+1)
            if s[j] == ch:
                j+=1
            if i==m or j == m:
                return True
        return False

