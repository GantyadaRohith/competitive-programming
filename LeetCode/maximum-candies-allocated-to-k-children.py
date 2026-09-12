class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        low,high = 1,sum(candies)//k
        while low<=high:
            mid = low+(high-low)//2
            temp = candies
            cnt = 0
            for i in temp:
                cnt += math.floor(i/mid)
            if cnt<k:
                high = mid -1
            else:
                low = mid+1
        return high