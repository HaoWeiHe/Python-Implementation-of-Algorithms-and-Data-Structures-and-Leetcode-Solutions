# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        if l1 < l2:
            cand = l1.val
            
        else:
            cand = l2.val

        res.next = Node(l1.val)
        res = res.next
        """
        
        dummy = head = ListNode(None)
        
        while l1 and l2:
            
            if l1.val < l2.val :
                can = l1.val
                l1 = l1.next
            else:
                can = l2.val
                l2 = l2.next
                
            dummy.next = ListNode(can)
            dummy = dummy.next
        if l1:
            dummy.next = l1
        if l2:
            dummy.next = l2
        return head.next
            