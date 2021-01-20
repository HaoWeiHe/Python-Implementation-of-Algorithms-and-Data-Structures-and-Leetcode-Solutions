# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        1->2->3->4->5->NULL
                         ^
        d ->5->4->3-> 2->1
        return d.next
        """
        d = ListNode()
        d.next = None
        while head:
            nxt = head.next
            tmp = d.next
            d.next = head
            head.next = tmp
            head = nxt
        return d.next