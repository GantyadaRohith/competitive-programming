class Solution:
    def minFlips(self, s: str) -> int:
        ss = s+s
        temps_1 = []
        temps_2 = []
        for i in range(len(ss)):
            if i%2 == 0:
                 temps_1.append('0')
                 temps_2.append('1')
            else:
                temps_1.append('1')
                temps_2.append('0')
        temps_1 = ''.join(temps_1)
        temps_2 = ''.join(temps_2)
        l = 0
        diff1 = 0
        diff2 = 0
        ans  = float('inf')
        n = len(s)
        for r in range(len(ss)):
            if ss[r] != temps_1[r]:
                diff1+=1
            if ss[r] != temps_2[r]:
                diff2+=1

            if r-l+1 > n:
                if ss[l] != temps_1[l]:
                    diff1 -= 1
                if ss[l] != temps_2[l]:
                    diff2 -= 1
                l += 1

            if r-l+1 == n:
                ans = min(ans,diff1,diff2)
        return ans