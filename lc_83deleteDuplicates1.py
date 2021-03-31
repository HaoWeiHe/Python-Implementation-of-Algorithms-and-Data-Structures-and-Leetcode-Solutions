# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, h):
        """
            1       1      2
       prev N               
       pren dummy
       
       
       1    1   2
     d 1        2
        """
        if not h:return h
        dummy = ListNode(h.val -1, next = h)
        cur = dummy
        while h:
            if h.val != cur.val:
                cur.next = h
                cur = cur.next
                
            h = h.next
        cur.next = None
        return dummy.next