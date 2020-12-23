# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        res, rem, car = ListNode(None), 0,0
        head = res
        while l1 or l2:
            val1 = 0 if not l1 else l1.val
            val2 = 0 if not l2 else l2.val
            car, rem = divmod(val1 + val2 + car, 10)
            nxt = ListNode(rem)
            res.next = nxt
            res = res.next
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        if car:
            nxt = ListNode(car)
            res.next = nxt
           
        return head.next