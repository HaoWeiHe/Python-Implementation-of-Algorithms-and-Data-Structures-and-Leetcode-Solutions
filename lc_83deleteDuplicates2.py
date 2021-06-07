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
        h = set()
        cur, prev = head, None
        while cur:
            if cur.val in h:
                prev.next = cur.next
            else:
                prev = cur
            h.add(cur.val)
            cur = cur.next
        return head
        
    def deleteDuplicates2(self, head):
        """
        1 1 1 1 2
        p       c
                p
        p c 
        """
        
        cur, prev  = head, None
        while cur:
            if prev and prev.val == cur.val:
                prev.next = cur.next
            else:
                prev = cur
            
            cur = cur.next
        return head
                
        