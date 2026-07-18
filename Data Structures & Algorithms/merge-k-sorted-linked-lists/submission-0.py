# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        res = ListNode(None)
        curr = res
        heap = []

        for i, node in enumerate(lists):
            heapq.heappush(heap, (node.val, i, node))
        
        while heap:
            val, pos, source = heapq.heappop(heap)
            curr.next = source
            curr = curr.next

            if source.next: heapq.heappush(heap, (source.next.val, pos, source.next))
        
        return res.next