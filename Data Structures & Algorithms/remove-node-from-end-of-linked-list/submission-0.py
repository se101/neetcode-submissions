# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # [1,2,3,4] n = 2
        dummy = ListNode(0, head)
        start, end = dummy, head
        for i in range(n):
            end = end.next 
        while end:
            start = start.next
            end = end.next
        start.next = start.next.next
        return dummy.next