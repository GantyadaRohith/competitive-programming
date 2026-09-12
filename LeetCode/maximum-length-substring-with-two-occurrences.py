class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        l = 0
        a = {}
        left = 0
        for i in range(len(s)):
            a[s[i]] = a.get(s[i],0)+1
            while a[s[i]]>2:
                a[s[left]]-=1
                left+=1
            l = max(l,i-left+1)
        return l
                