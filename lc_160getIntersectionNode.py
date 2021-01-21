# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        head A-> headB
        headB-> headA
        
        a + c + b = b + c + a
        """
        Apre, Bpre = ListNode(), ListNode()
  
        p1, p2 = headA, headB
        flag = 0
        while p1 != p2 and flag <2:
           
            if p1 and p1.next:
                p1 = p1.next
            else:
                p1 = headB
                flag += 1
                
            if p2 and p2.next:
                p2 = p2.next
            else:
                p2 = headA
            
        
        return p1 if flag<2 else None
    def getIntersectionNode2(self, headA, headB):
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
            
