# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
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
                
        