# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        maxi = -float('inf')
        def dfs(node):
            nonlocal maxi
            left_gain,right_gain = 0,0
            if node.left is not None:
                left_gain = max(dfs(node.left), 0)
            if node.right is not None:
                right_gain = max(dfs(node.right), 0)
            ans = left_gain + node.val + right_gain
            maxi = max(maxi,ans)
            return node.val + max(left_gain, right_gain)
        dfs(root)
        return maxi