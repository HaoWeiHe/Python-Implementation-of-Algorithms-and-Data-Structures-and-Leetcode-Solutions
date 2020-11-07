
class Solution(object):
    def sortedListToBST(self,head):
        def getMid(head):
            slow, fast = head, head
            preSlow = None
            while fast and fast.next:
                preSlow = slow
                fast = fast.next.next
                slow  = slow.next
            if preSlow:
                preSlow.next = None
            return slow

        def dfs(head):
            
            if not head: return None

            mid = getMid(head)
            root =  TreeNode(mid.val)
            if head == mid: 
                return root

            root.left = dfs(head)
            root.right = dfs(mid.next)
            return root
        return dfs(head)

    def sortedListToBST_sol1(self, head):
       
        lst = []
        while head:
            lst.append(head.val)
            head =head.next
        
        def dfs(lst):
            if not lst: 
                return 
            mid = len(lst)/2
            root = TreeNode(lst[mid])
            root.right = dfs(lst[mid+1:])
            root.left = dfs(lst[:mid])
            return root
        
        return dfs(lst)
            
        