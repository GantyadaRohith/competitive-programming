class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0]*(n+1)
        dp[0] = 0
        j = 1
        for i in range(1,n+1):
            if i%(2**j) == 0:
                dp[i] = 1
                j+=1
            else:
                temp = i
                cnt = 0
                while i:
                    if i&1:
                        cnt+=1
                    i = i>>1
                dp[temp] = cnt
        return dp