# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        current = head
        length = 0
        while not current == None:
            length += 1
            current = current.next
        mid = length // 2 
        current = head
        for n in range(mid):
            current = current.next
        return current
