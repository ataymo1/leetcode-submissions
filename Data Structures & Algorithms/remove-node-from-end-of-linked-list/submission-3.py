# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        count = 1

        node = head

        while node.next:
            count += 1
            node = node.next

        if count == 1:
            return None
        
        if count == n:
            return head.next
        node = head
        for i in range(count - n - 1):
            if not node.next.next:
                node.next = NULL
            node = node.next
        
        node.next = node.next.next

        return head



        

        