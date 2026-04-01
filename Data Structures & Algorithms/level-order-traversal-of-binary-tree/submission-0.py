# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []
        
        queue = deque()
        levels = []
        
        queue.append(root)
        levels.append([root.val])

        while len(queue) > 0:
            level = []
            for i in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                    level.append(node.left.val)
                if node.right:
                    queue.append(node.right)
                    level.append(node.right.val)
            if len(level) > 0:
                levels.append(level)
        return levels

        