# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr = self.inOrder(root)

        return arr[k-1]

    def inOrder(self, root):
        sol = []

        if not root:
            return []
        
        if root.left:
            sol += self.inOrder(root.left)
        
        sol.append(root.val)

        if root.right:
            sol += self.inOrder(root.right)
        
        return sol
        

            