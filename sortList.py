
class Solution:
    def sortList(self, head):

        if not head or not head.next:
            return head

        pre, fast, slow = None, head, head

        

        while(fast and fast.next):
            pre, fast, slow = slow, fast.next.next,slow.next
            # slow = slow.next

        fast = slow
        pre.next = None


        # self.sortList(head)
        # self.sortList(slow)
        return self.merge(self.sortList(head), self.sortList(slow))

        # return self.merge(*map(self.sortList, (head, slow)))
        



    def merge(self, slow, fast):

        dummy = tail = ListNode(None)
       
        while slow and fast:
         
            if slow.val > fast.val:
                tail.next = fast
                tail = fast
                fast = fast.next
            else:
                tail.next = slow
                tail = slow
                slow = slow.next


        tail.next = fast or slow
        
        return dummy.next



