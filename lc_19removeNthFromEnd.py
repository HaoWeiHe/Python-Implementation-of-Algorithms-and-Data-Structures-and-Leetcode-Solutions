# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(None, head)
        self.prev, self.d = dummy, None
        
        def dfs(node):
            if not node:
                return 0
            
            i = dfs(node.next) + 1
            if i == n:
                self.d = node
            if i == n+1:
                self.prev = node
            return i
        dfs(head)
        
        self.prev.next = self.d.next
        return dummy.next

    def removeNthFromEnd2(self, head, n):
        """
        1) use recursive
        2) use iterated
        """
        dummy = ListNode(None, head)
        prev = dummy
        slow, fast = head, head
        for _ in range(n):
            fast = fast.next
        while fast:
            fast = fast.next
            prev = slow
            slow = slow.next
        prev.next = slow.next
        return dummy.next