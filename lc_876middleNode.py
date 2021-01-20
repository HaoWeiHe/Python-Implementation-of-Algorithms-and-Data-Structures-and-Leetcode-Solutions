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
        c = 0 
        d = head
        while head:
            c +=1
            head = head.next
        mid = c/2 + 1
        c = 1
        while d:
            if c == mid:return d
            c +=1
            d = d.next