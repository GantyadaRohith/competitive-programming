class Solution:
    def numTrees(self, n: int) -> int:
        if n<=1:
            return 1
        dp = [0]*(n+1)
        dp[0] = 1
        for i in range(1,n+1):
            temp = (2*(2*i-1))/(i+1)
            dp[i] = dp[i-1]*temp
        return (int(dp[-1]))