# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        1. reverse in half way in place
        2. two pointer 
        
        """
        def findHalf():
            first = ListNode()
            first.next = head
            #1 -> itself 2 -> first
            if not first.next or not first.next.next:
                return head
            slow, fast = first.next, first.next.next
            while fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next
            
            return slow
        
        def reverse(cur):
            """
             3-2-1-Null
                 ^ 
            """
            
            pre = None
            while cur:
                nxt = cur.next
                cur.next = pre
                pre = cur
                cur = nxt
            
            return pre
        """
        1->2->1<-2
        """
        if not head:return True
        first_end = findHalf()
        sec_start = first_end.next
        
        first_end.next = None
        
        sec_start = reverse(sec_start)
        
        while head and sec_start:
            if head.val != sec_start.val:
                return False
            sec_start = sec_start.next
            head = head.next
        return True
        