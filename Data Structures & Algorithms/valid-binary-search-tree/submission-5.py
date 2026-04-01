# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        if not root:
            return True

        return self.check(root.left, None, root.val) and self.check(root.right, root.val, None)
        
    def check(self, node, lower, upper):
        if not node:
            return True
        print(f"{lower} : {upper}")
        val = node.val
    # 4 cases
    # 1. rightmost - no upper
    # 2. leftmost - no lower
    # 3. right left - already has upper, need to apply lower
    # 4. left right - already has lower, need to apply upper

        if upper is not None:
            if val >= upper:
                return False
        if lower is not None:
            if val <= lower:
                return False
        
        return self.check(node.left, lower, val) and self.check(node.right, val, upper)
        




        