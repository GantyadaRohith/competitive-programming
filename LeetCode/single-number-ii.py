class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a = {}
        for i in nums:
            a[i] = a.get(i,0) + 1
        print(a)
        for i,j in enumerate(a.items()):
            print(i,j)
            if j[1]== 1:
                return j[0]
        