# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        1   2   3   4   5   6
        prv cur next
        1<-2
  
        1   3   2   4   5   6
                cur next
                
        1   4   3   2   5   6
        
        """
          
        if not head :return head
        dummy = ListNode()
        dummy.next = head
        prev = dummy
        
        for i in range(left-1):
            prev = prev.next
        cur = prev.next
        
        for _ in range(right-left ):
            next = cur.next
            cur.next = next.next
            next.next = prev.next
            prev.next = next
       
        return dummy.next