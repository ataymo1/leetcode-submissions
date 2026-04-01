# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        res = 0

        def bfs(node, depth):
            nonlocal res
            res = max(res, depth)

            if node.left:
                bfs(node.left, depth + 1)
            if node.right:
                bfs(node.right, depth + 1)

        if root:
            bfs(root, 1)
        return res
        