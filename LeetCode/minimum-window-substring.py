class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m=len(s)
        n=len(t)
        if m<n:
            return ""
        dic={}
        for c in t:
            dic[c]=dic.get(c,0)+1
        req=len(dic)
        formed=0
        left=0
        win={}
        start=0
        minlen=float('inf')
        for r in range(len(s)):
            win[s[r]] = win.get(s[r], 0) + 1
            if s[r] in dic and win[s[r]]==dic[s[r]]:
                formed+=1
            while formed==req:
                if r-left+1<minlen:
                    minlen=r-left+1
                    start=left
                win[s[left]]-=1
                if s[left] in dic and win[s[left]] <dic[s[left]] :
                    formed-=1
                left+=1
        return "" if minlen==float('inf') else s[start:start+minlen]