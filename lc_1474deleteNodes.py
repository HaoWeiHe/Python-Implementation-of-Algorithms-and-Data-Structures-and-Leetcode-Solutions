# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteNodes(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        #delete(m+1, m+n)
        link m - m+n+1, m start from 1
        
        [1,2,3,4,5,6,7,8,9,10,11,12,13], 
         1 2 3 4 5 6 
                  ^
           2 
               n
             3 
        """
        
        d = head
        c = 0
        while head:
            c += 1
            if m ==c:
                for _ in range(n):
                    if head.next:
                        head.next = head.next.next
                c = 0
            head = head.next
        return d