# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def sortedListToBST(self, head):
        """
         [-10,-3,0,5,9]
         -10 -3 0 5 9 
         mid:       0 
           [-10,-3]    [5,9]
            (-10)
               -3
        """
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
            
        