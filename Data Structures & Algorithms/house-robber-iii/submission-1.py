# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        return max(self.dfs(root))


        
    def dfs(self, node):
        if not node:
            return tuple((0, 0))
        
        left_taken, left_skipped = self.dfs(node.left)
        right_taken, right_skipped = self.dfs(node.right)

        robbed = node.val + left_skipped + right_skipped
        skipped = max(left_skipped, left_taken) + max(right_skipped, right_taken)

        return tuple((robbed, skipped))






