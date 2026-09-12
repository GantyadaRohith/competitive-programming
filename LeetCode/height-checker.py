class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        x = sorted(heights)
        j = 0
        for i in range(len(x)):
            if heights[i] != x[i]:
                j+=1
        return j