# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        curr = slow.next
        slow.next, prev = None, None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        point = head
        while prev:
            temp1 = point.next
            temp2 = prev.next
            point.next = prev
            prev.next = temp1
            point = temp1
            prev = temp2
