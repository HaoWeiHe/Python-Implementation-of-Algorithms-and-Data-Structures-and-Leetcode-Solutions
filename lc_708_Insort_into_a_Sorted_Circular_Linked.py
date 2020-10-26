"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution(object):
    def insert(self, head, insertVal):
        """
        :type head: Node
        :type insertVal: int
        :rtype: Node
        """
        #consider corner case 
        #1. if head not exist ->  create a new single circular list and return the reference to that single node. 
        #2. if insertVal > than the maxVal
        #3. if insertVal < minVal
        # Case 2 & 3 can use the same approach : pre.next = NewCreatedNode, NewCreatedNode.next= cur
        if not head:
            head = Node(insertVal)
            head.next = head
            return head
        pre, cur = head, head.next

        while cur != head:
            if pre.val <= insertVal <= cur.val:
                break
            #abnormal happend when cur.val < pre.val #a turning point
            if cur.val < pre.val and (pre.val <= insertVal or cur.val >= insertVal) :
                break
            pre = cur
            cur = cur.next

        pre.next = Node(insertVal, cur) 
        return head



      