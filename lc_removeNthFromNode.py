# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        
        count = 0
        res = dummy = ListNode(0)
        res.next = dummy.next = head
        
        
        while head:
            count += 1
            head = head.next
           
        if count < n: return None
        
        m = count -n
        
        for i in range(m):
            
            dummy = dummy.next
        
        
        
        if dummy.next:
            tmp = dummy.next.next

            dummy.next = tmp
        else:
            dummy.next = None

        return res.next
        