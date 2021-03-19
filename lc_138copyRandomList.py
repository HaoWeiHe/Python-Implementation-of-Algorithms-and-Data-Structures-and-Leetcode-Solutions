"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        head_cp = head
        h = {}
        while head:
            node = Node(head.val, None, None)
            h[head] = node
            head = head.next
        h[None] =  None
        head = head_cp
        
        while head:
            cur = h[head]
            cur.next = h[head.next]
            cur.random = h[head.random]
            head = head.next
        return h[head_cp]
# """
# # Definition for a Node.
# class Node:
#     def __init__(self, x, next=None, random=None):
#         self.val = int(x)
#         self.next = next
#         self.random = random
# """

# class Solution(object):
#     def __init__(self):
#         self.record = {}
        
#     def copyRandomList(self, h):
#         """
#         :type head: Node
#         :rtype: Node
#         """
#         if not h:
#             return h
        
#         if h in self.record:
#             return self.record[h]
        
#         cur = Node(h.val, None, None)
        
#         self.record[h] = cur
#         cur.next = self.copyRandomList(h.next)
#         cur.random = self.copyRandomList(h.random)
#         return cur