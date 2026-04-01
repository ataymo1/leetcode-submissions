# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.cur_node = root
        self.stack = []

    def next(self) -> int:
        while self.cur_node:
            self.stack.append(self.cur_node)
            self.cur_node = self.cur_node.left
        
        temp = self.stack.pop()
        self.cur_node = temp.right
        return temp.val
        
        

    def hasNext(self) -> bool:
        return True if self.stack or self.cur_node else False
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()