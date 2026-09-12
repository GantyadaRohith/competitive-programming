class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def splits(num,n):
            x = 1
            s = 0
            for i in range(len(num)):
                if s+num[i]<=n:
                    s+=num[i]
                else:
                    x+=1
                    s = num[i]
            return x
        low = max(nums)
        high = sum(nums)
        while low<= high:
            mid = low + (high-low)//2
            split = splits(nums,mid)
            if split<=k:
                high = mid-1
            else:
                low = mid+1
        return low
