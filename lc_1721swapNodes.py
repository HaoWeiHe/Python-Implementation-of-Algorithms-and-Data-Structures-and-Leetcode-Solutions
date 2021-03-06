# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapNodes(self, head, k):
        """
        change the value at nodeA and nodeB
        """
        dummy = head
        l = 0
        while dummy:
            l +=1
            dummy = dummy.next
        lst = [None, None]
        dummy = head
        for c in range(1, max(k, l-k+1)+1):
            if c == k:
                lst[0] = dummy
            if c == l-k+1:
                lst[1] = dummy
            dummy = dummy.next
       
        lst[0].val, lst[1].val = lst[1].val, lst[0].val
        return head