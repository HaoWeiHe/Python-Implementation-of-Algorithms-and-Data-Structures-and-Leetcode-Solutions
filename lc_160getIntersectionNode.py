# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, a, b):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        p1, p2 = a,b
        while p1 != p2:
            p1 = p1.next if p1 else b
            p2 = p2.next if p2 else a
        return p1