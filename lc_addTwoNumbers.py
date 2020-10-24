ddTwoNumbers(self, l1, l2): 
        
        carry = 0
        root = node = ListNode(0)

        while  l1 or l2 or carry :
            
            l1_val = l2_val = 0
            
            
            if l1:
                l1_val = l1.val
                l1 = l1.next
            if l2:
                l2_val = l2.val
                l2 = l2.next
                
            val = (l1_val + l2_val + carry ) % 10
            carry = (l1_val + l2_val + carry ) / 10


            node.next = ListNode(val)
            node = node.next
        return root.next
