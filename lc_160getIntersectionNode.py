
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        a = set()
        while headA:
            a.add(headA)
            headA = headA.next
        
        while headB:
            if headB in a: return headB
            headB = headB.next
            
