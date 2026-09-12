class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if len(nums) == 1:
            return False
        pre = [nums[0]]
        for i in range(1,len(nums)):
            pre.append(pre[-1]+nums[i])
        a = defaultdict(list)
        for i in range(len(pre)):
            pre[i] = pre[i]%k
            if pre[i] == 0 and i>=1:
                return True
            a[pre[i]].append(i)
        f = 0
        for i,j in a.items():
            if len(j) >= 2:
                if max(j)-min(j)>=2:
                    f = 1
                    break
        return False if f == 0 else True
               
        