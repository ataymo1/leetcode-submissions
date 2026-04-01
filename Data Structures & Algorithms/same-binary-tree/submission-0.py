# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        

        if not p:
            if not q:
                return True
            else:
                return False
        else:
            if not q:
                return False
        
        if p.val != q.val:
            return False
        
        if not p.left and q.left or not q.left and p.left:
            return False
        if not p.right and q.right or not q.right and p.right:
            return False

        if not p.left and not q.left and not p.right and not p.left:
            return True
        
        
        return self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left)