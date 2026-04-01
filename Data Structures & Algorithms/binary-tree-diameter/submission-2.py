# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        #will return max right and left
        if not root:
            return 0
        diameter = 0

        def dfs(node, depth):
            nonlocal diameter
            max_left, max_right = depth, depth

            if node.left:
                max_left = dfs(node.left, depth + 1)
            if node.right:
                max_right = dfs(node.right, depth + 1)

            diameter = max(diameter, (max_right + max_left) - 2*depth)
            
            return max(max_right, max_left)
        
        dfs(root, 0)
        return diameter


            
