class Solution:
    def searchInsert(self, n: List[int], t: int) -> int:
        l,r = 0,len(n)
        f = False
        while l<r:
            mid = (l+r)//2
            if n[mid] == t:
                f = True
                return mid
            elif t>n[mid]:
                l=mid+1
            else:
                r=mid
        return l