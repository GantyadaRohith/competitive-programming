class Solution:
    def maxArea(self, height: List[int]) -> int:
        l,r = 0,len(height) - 1
        maxi = 0
        while(l<r):
            area = (r-l) *min(height[l],height[r])
            maxi = max(maxi,area)
            if height[l]>=height[r]:
                r-=1
            else:
                l+=1
        return maxi