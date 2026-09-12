class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        temp = sorted(score,reverse = True)
        a = {}
        g,s,b = 0,0,0
        j = 0
        for i in temp:
            if g == 0:
                a[i] = 'Gold Medal'
                g+=1
                j+=1
            elif s == 0:
                a[i] = 'Silver Medal'
                s+=1
                j+=1
            elif b == 0:
                a[i] = 'Bronze Medal'
                b+=1
                j+=1
            else:
                j+=1
                a[i] = str(j)
        out = []
        for i in score:
            out.append(a[i])
        return out
        