# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicatesUnsorted(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        
        """
        h = defaultdict(int)
        d = head
        dummy = ListNode(None, head)
        p = dummy
        while d:
            h[d.val] += 1
            d = d.next
        
        while head:
            if h[head.val] > 1:
                p.next = head.next
            else:
                p = head
           
            head = head.next
        return dummy.next
                