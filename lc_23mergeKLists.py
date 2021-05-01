# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lsts):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lsts:return None
        if len(lsts) == 1: 
            return lsts[0]
        mid = len(lsts) /2
        leftpart =  self.mergeKLists(lsts[:mid])
        rightpart = self.mergeKLists(lsts[mid:])
        return self.merge(leftpart, rightpart)
    
    def merge(self, lf, rt):
        
        dum = head = ListNode()
        while lf and rt:

            if lf.val < rt.val:
                head.next = lf
                lf = lf.next
            else:
                head.next = rt
                rt =rt.next
            head = head.next
        while lf:
            head.next = lf
            lf = lf.next
            head = head.next
        
        while rt:
            head.next = rt
            rt = rt.next
            head = head.next
        return dum.next
         