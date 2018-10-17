

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        if not head :
            return head
        
    
        cur = head
        nxt = head.next
        prev = None
        
        while(nxt):
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
            nxt = cur.next

       
        cur.next = prev
        return cur
