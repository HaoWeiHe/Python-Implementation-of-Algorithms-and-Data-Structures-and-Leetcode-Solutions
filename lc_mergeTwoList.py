# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        res = root =  ListNode(None)
        
        
        while(  l1 or  l2):
            # print(l1.val)
            
            
            if not l1 :
                res.next = ListNode(l2.val)
                res = res.next
                l2 = l2.next
            elif not l2:
                res.next = ListNode(l1.val)
                res = res.next
                l1 = l1.next
           
            elif l1.val >= l2.val:
                res.next = ListNode(l2.val)
                res = res.next
                l2 = l2.next
            else:
                res.next = ListNode(l1.val)
                res = res.next
                l1 = l1.next
                
        return root.next