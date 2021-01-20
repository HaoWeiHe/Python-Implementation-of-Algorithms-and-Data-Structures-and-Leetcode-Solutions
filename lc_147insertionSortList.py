# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        rh = ListNode()
        rh.next = None
        # 4->2->1->3
        def helper(node):
            r = rh
            while r.next:
                if r.next.val > node.val:
                    tmp = r.next
                    r.next = node
                    node.next = tmp
                    return 
                r = r.next
            r.next = node
            node.next = None
            
   
        while head:
            nxt  = head.next
            helper(head)
            head = nxt
        return rh.next