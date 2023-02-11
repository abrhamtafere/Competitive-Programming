# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        self.pointer = head
        def check(current_node = head):
            if current_node is not None:
                if not check(current_node.next):
                    return False
                if self.pointer.val != current_node.val:
                    return False
                self.pointer = self.pointer.next
            return True
        return check()
