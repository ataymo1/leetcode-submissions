# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        heap = []
        if not lists or len(lists) == 0:
            return None
        
        head = None
        cur = None
        for i in range(len(lists)):
            node = lists[i]
            heapq.heappush(heap, (node.val, i, node))
        popped = heapq.heappop(heap)
        head = popped[2]
        cur = head
        if cur.next:
            heapq.heappush(heap, (cur.next.val, popped[1], cur.next))

        while heap:
            val, i, node = heapq.heappop(heap)
            cur.next = node
            cur = cur.next
            if node.next:
                heapq.heappush(heap, (node.next.val, i , node.next))
        return head

            

        
        