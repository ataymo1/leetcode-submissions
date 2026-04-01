# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        plist = self.find(root, p, [])
        qlist = self.find(root, q, [])
        node = None
        
        for p, q in zip(plist, qlist):
            if p[0] == q[0]:
                node = p[1]
        
        return node
                


    def find(self, cur, target, path):
        path.append((cur.val, cur))
        if target.val == cur.val:
            return path


        if target.val > cur.val:
            return self.find(cur.right, target, path)
        else:
            return self.find(cur.left, target, path)

