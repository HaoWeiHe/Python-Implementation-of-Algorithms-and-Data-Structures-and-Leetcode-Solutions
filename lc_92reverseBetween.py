# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def reverseBetween(self, head, m, n):
        """

        """
        pre, dummy, hold = ListNode(None), head, None
        pre_head = ListNode(None)
        counter = 1
        lst  = []
        
        while dummy:
            if counter < m:
                pre = dummy
            if m <= counter <n:
                lst.append(dummy)   
                
            if counter == n:
                
                hold = dummy.next
                if pre.val == None:
                    head = dummy
                pre.next = dummy
                pre = pre.next
                while lst:
                    pre.next = lst.pop()
                    pre = pre.next
                pre.next = hold
    
                return head 
            counter +=1
            
            dummy = dummy.next
