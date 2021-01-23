# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
           [
              1->4->5,
              1->3->4,
              2->6
            ]
        h -> 1 
        end if all pointer is None
        """
        dum = ListNode()
        res = dum
        
        while True:
            swap = None
            for cur in range(len(lists)):
                
                if not lists[cur]: continue
                
                if swap is None:
                    swap = cur
                if lists[swap].val > lists[cur].val:
                    swap = cur
           
            if swap == None:
                return res.next
            
            tmp = lists[swap].next
            lists[swap].next = None
            dum.next = lists[swap]
            dum = dum.next
            lists[swap] = tmp
          