class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        s.split()
        perm = [0]*(len(s)+1)
        x=0
        y = len(s) 
        for i in range(len(s)):
            if s[i] == 'I':
                perm[i] = x
                x+=1
            elif s[i] == 'D':
                perm[i] = y
                y-=1
        perm[len(s)] = x
        return perm