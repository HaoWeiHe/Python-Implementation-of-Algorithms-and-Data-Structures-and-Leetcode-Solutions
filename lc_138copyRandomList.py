
class Solution(object):
    def copyRandomList(self, head):
        if not head:return head
        ch = head
        while head:
            node = Node(head.val, None, None)
            # tmp = head.next
            node.next = head.next
            head.next = node
            head = node.next
        head = ch
        
        while head:
            head.next.random = head.random.next if head.random else None
            head = head.next.next

        
        old_list = ch
        new_list = ch.next
        head_new = ch.next
        while old_list :
            old_list.next = old_list.next.next
            new_list.next = new_list.next.next if new_list.next else None
            old_list = old_list.next
            new_list = new_list.next
        return head_new
# """
# # Definition for a Node.
# class Node:
#     def __init__(self, x, next=None, random=None):
#         self.val = int(x)
#         self.next = next
#         self.random = random
# """

# class Solution(object):
#     def copyRandomList(self, head):
#         """
#         :type head: Node
#         :rtype: Node
#         """
#         ch = head
#         while head:
#             node = Node(head.val, None, None)
            
#             tmp= head.next
#             head.next = node
#             node.next = tmp
#             head = tmp
#         head = ch
        
#         while head :
#             if not head.random:
#                 head.next.random = None
#             else:
#                 head.next.random = head.random.next
#             tmp = head.next.next
#             if not head.next.next:
#                 head.next = None
#             else:
#                 head.next= head.next.next.next
#             head = tmp
#         return ch.next
            
# # """
# # # Definition for a Node.
# # class Node:
# #     def __init__(self, x, next=None, random=None):
# #         self.val = int(x)
# #         self.next = next
# #         self.random = random
# # """

# # class Solution(object):
# #     def copyRandomList(self, head):
# #         """
# #         :type head: Node
# #         :rtype: Node
# #         """
# #         head_cp = head
# #         h = {}
# #         while head:
# #             node = Node(head.val, None, None)
# #             h[head] = node
# #             head = head.next
# #         h[None] =  None
# #         head = head_cp
        
# #         while head:
# #             cur = h[head]
# #             cur.next = h[head.next]
# #             cur.random = h[head.random]

# #             head = head.next
# #         return h[head_cp]
# # # """
# # # # Definition for a Node.
# # # class Node:
# # #     def __init__(self, x, next=None, random=None):
# # #         self.val = int(x)
# # #         self.next = next
# # #         self.random = random
# # # """

# # # class Solution(object):
# # #     def __init__(self):
# # #         self.record = {}
        
# # #     def copyRandomList(self, h):
# # #         """
# # #         :type head: Node
# # #         :rtype: Node
# # #         """
# # #         if not h:
# # #             return h
        
# # #         if h in self.record:
# # #             return self.record[h]
        
# # #         cur = Node(h.val, None, None)
        
# # #         self.record[h] = cur
# # #         cur.next = self.copyRandomList(h.next)
# # #         cur.random = self.copyRandomList(h.random)
# # #         return cur