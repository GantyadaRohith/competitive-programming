class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        def isPrime(n):
            if n<=1:
                return False
            if n ==2 :
                return True
            if n%2 == 0:
                return False
            for i in range(3,math.ceil(n**0.5)+1):
                if n%i == 0:
                    return False
            return True
        out = []
        for i in range(len(nums)):
            if isPrime(nums[i][i]):
                out.append(nums[i][i])
            if isPrime(nums[i][len(nums)-i-1]) and i!=len(nums)-i-1:
                out.append(nums[i][len(nums)-i-1])
        return max(out) if out else 0
            