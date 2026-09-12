class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if(m*k) > len(bloomDay):
            return -1
        low = min(bloomDay)
        high = max(bloomDay)
        while low <= high:
            mx = low + (high-low)//2
            cnt,mi = 0,0
            for i in range(len(bloomDay)):
                if bloomDay[i]<=mx:
                    mi+=1
                else:
                    mi=0
                if mi==k:
                    cnt+=1
                    mi=0
            if cnt>=m:
                high = mx-1
            else:
                low = mx+1
        return low