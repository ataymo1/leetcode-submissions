"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        qset = dict()

        while q:
            qset[q.val] = q
            q = q.parent

        while p:
            if p.val in qset:
                return qset[p.val]
            p = p.parent



        
    