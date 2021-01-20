"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
        
3 possitble position 
1) pre & post both larger than val
2) pre & post both less than val
3) pre < val < post
    
"""

class Solution(object):
    def insert(self, head, insertVal):
        """
        :type head: Node
        :type insertVal: int
        :rtype: Node
        """
        if not head:
            newW = Node(insertVal)
            newW.next = newW
            return newW
        
        def helper(node):
            nxt = node.next
            newN = Node(insertVal)
            node.next = newN
            newN.next = nxt
 

        mx = head
        while mx.next != head and mx.val <= mx.next.val:
            mx = mx.next
            
        mn = mx.next
        
        if mx.val <= insertVal or mn.val >=  insertVal:
            helper(mx)
        else:
            cur = mn
          
            while cur.next.val < insertVal:
                cur = cur.next
            helper(cur)
        return head

