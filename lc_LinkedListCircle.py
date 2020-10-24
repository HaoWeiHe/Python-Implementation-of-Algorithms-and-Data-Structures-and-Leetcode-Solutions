# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        
    #if head == null or head.next ==null return False
    #if n.fast==n.slow return True
    
        if head == None or head.next == None :
            return False
    
        fast = slow = head
    
        while(fast and fast.next):
            fast = fast.next.next
            slow = slow.next
        
            if (fast == slow):
                return True
        
        return False


