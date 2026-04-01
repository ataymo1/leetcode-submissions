# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        sol = []
        if not root:
            return sol
        sol.append(root.val)
        if root.left:
            sol += (self.preorderTraversal(root.left))
        if root.right:
            sol += (self.preorderTraversal(root.right))
        return sol
