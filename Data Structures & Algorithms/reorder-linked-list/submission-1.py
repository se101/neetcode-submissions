# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        curr = slow.next
        prev = slow.next = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        start, end = head, prev
        while end:
            temp1 = start.next
            temp2 = end.next
            start.next = end
            end.next = temp1
            start = temp1
            end = temp2
        