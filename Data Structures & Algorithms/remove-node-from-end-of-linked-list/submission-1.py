# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr, curr1 = head, head
        length = 0
        while curr:
            curr = curr.next
            length+=1
        if n==length:
            return head.next
        target = length-n-1
        while target>0:
            curr1 = curr1.next
            target-=1

        temp = curr1.next
        curr1.next = curr1.next.next
        temp.next = None

        return head
        
        