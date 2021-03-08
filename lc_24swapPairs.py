# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
     d   1   2   3   4
     cur pre tar  

     cur = pre
     d   2   1   3   4

            cur     tar
     d   2   1   4   3
     
        """
        if not head or not head.next: return head
        
        dum  = ListNode(None)
        dum.next = head
        cur, pre, tar = dum, dum.next, dum.next.next
        
        while 1:
            tmp = tar.next
            cur.next = tar
            tar.next = pre
            pre.next = tmp
            if pre.next and pre.next.next:
                cur = pre
                tar = cur.next.next  
                pre = cur.next
            else: break
        return dum.next