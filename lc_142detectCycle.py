# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        def inters():
            slow, fst = head, head

            while fst.next and fst.next.next :

                slow = slow.next
                fst = fst.next.next
                if fst == slow:
                    return slow
            return None
        
        if not head or not head.next:return None
        
        fst = inters()
        
        if not fst:return None
        
        slow = head
        while slow!=fst:
            slow = slow.next
            fst = fst.next
        return slow