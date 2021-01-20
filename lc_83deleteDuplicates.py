# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head: return 
        d = head
        preV = ListNode(head.val -1)
        while head:
            if preV.val== head.val:
                preV.next = head.next
            else:
                preV = head
            head = head.next
        return d