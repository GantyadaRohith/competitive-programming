class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        memo = {}
        def solve(l, r):
            if l > r:
                return 0
            if memo.get((l,r),0):
                return memo[(l,r)]
            left = piles[l] - solve(l + 1, r)
            right = piles[r] - solve(l, r - 1)
            memo[(l,r)] = max(left,right)
            return memo[(l,r)]
            
        a = solve(0,len(piles)-1) 
        if a>=0:
            return True
        else:
            return False 