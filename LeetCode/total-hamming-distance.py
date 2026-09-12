class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        total = 0
        n = len(nums)
        
        for bit in range(32):
            count1 = 0
            for num in nums:
                if num & (1 << bit):
                    count1 += 1
                    
            count0 = n - count1
            total += count1 * count0
            
        return total
