# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        1) use recursive
        2) use iterated
        """
        dummy = ListNode(None, head)
        prev = dummy
        slow, fast = head, head
        for _ in range(n):
            fast = fast.next
        while fast:
            fast = fast.next
            prev = slow
            slow = slow.next
        prev.next = slow.next
        return dummy.next