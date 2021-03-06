
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, h):
        """
         # [1,2,3,3,4,4,5,6]
         #                h
         #    p ------->5  
         #              p

         [1,2,3,3,4,4,5,6]
                         h
            p-------> 5
                      p
        """
        
        dummy = ListNode(None, h)
        pre = dummy
        while h:
            if h.next and h.val == h.next.val:
                while h.next and h.val == h.next.val:
                    h = h.next
                pre.next  = h.next
            else:
                pre = h

            h = h.next
        return dummy.next

    def deleteDuplicates2(self, head):
        """
        [1,2,3,3,4,4,5]
   c                 v
   p       p
               at this point, p back to Node2
   h = {1:dummy,2:Node1,3:Node2, 4: Node2}
        [1,1,1,2,3]
    c    v
    p  v
    h = {1:dummy}
    
        """
        dummy = ListNode(None, head)
        prev, cur = dummy, head
        h = {}

        while cur :
            if cur.val in h:
                prev = h[cur.val]
                prev.next = cur.next
            else:
                h[cur.val] = prev
                prev = cur
            
            cur = cur.next
        return dummy.next
        
        