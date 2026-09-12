class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        maxlen=0
        se=set()
        for i in range(len(s)):
            while s[i] in se:
                se.remove(s[left])
                left+=1
            se.add(s[i])
            maxlen=max(i-left+1,maxlen)
        return maxlen
