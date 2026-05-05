"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        nodes = {}

        if not head:
            return None
        
        cur = head
        copy = Node(cur.val)
        new_head = copy

        while cur:
            # check if next node exits
            nodes[cur] = copy

            if not cur.next:
                copy.next = None
            elif cur.next in nodes:
                copy.next = nodes[cur.next]
            else:
                copy.next = Node(cur.next.val)
                nodes[cur.next] = copy.next

            # check if random node exits

            if not cur.random:
                copy.random = None
            elif cur.random in nodes:
                copy.random = nodes[cur.random]
            else:
                copy.random = Node(cur.random.val)
                nodes[cur.random] = copy.random
            
            # if copy and cur:
            #     print(f"{cur.val} : {copy.val}")
            #     if copy.next and cur.next:
            #         print(f"{cur.next.val} : {copy.next.val}")
            #     if copy.random and cur.random:
            #         print(f"{cur.random.val} : {copy.random.val}")
            #     print("---------------------")
            
            cur = cur.next
            copy = copy.next


        return new_head


        
        