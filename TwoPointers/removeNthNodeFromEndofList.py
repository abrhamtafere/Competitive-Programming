# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head: return head
        slow=fast=head
        while k:
            fast=fast.next
            k-=1
        if not fast: return head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next
        slow.next=slow.next.next
        return head
