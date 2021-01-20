# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        1->2->6->3->4->5->6, 
                       ^   
        """
       
        d = pre = ListNode()
        pre.next = head
       
        while head:
            if head.val == val:
                pre.next = head.next
            else:
                pre = head
            head = head.next
        return d.next