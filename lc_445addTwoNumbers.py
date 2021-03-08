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
        def rev(head):
            last = None
            while head:
                tmp = head.next
                head.next = last
                last = head
                head = tmp
            return last

        l1 = rev(l1)
        l2 = rev(l2)
        
        head = None
        carry = 0
        while l1 or l2:
            a = l1.val if l1 else 0
            b = l2.val if l2 else 0
            carry, val = divmod(a + b + carry, 10)
            cur = ListNode(val)
            cur.next = head
            head = cur
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
        if carry:
            cur = ListNode(carry)
            cur.next = head
            head = cur
        return head