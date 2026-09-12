# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countDominantNodes(self, root):
        cnt = 0
        def dfs(node):
            if not node:
                return float("-inf"), 0
            lm,lc = dfs(node.left)
            rm,rc = dfs(node.right)
            maxi = max(node.val, lm, rm)
            cnt = lc + rc
            if node.val == maxi:
                cnt += 1
            return maxi, cnt
        maxi,cnt = dfs(root)
        return cnt