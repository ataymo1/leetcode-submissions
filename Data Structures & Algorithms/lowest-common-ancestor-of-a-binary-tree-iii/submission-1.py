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
        
        dummyq = q
        dummyp = p

        while dummyq != dummyp:
            if dummyq:
                dummyq = dummyq.parent
            else:
                dummyq = p
            if dummyp:
                dummyp = dummyp.parent
            else:
                dummyp = q
        return dummyq




        
    