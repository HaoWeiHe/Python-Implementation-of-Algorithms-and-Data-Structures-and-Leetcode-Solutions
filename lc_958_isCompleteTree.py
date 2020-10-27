# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isCompleteTree(self, root):
        """
        Check the all the situation of levels.
        assume, we have N levels,
        1 ~ N-1 levels should be full_of_1
        N could be a list of having increasing number(here we only have 0 and 1) 

        """

        
        def validate(lst):

            if  not lst: return True
            
            for idx, sublst in enumerate(lst[:-1]):
                    if not all(sublst): 
                        return False

            pre = lst[-1][0]
            
            for e in lst[-1]:
                if pre < e:
                    return False
                pre = e
            return True

        if not root: return 
        q = [root] 
        all_check = []
        while q:
            tmp_length = len(q) 
            check = []
            
            for _ in range(tmp_length): 
                cur = q.pop(0) #1
                if cur.left:
                    q.append(cur.left)
                    check.append(1)
                else:
                    check.append(0)

                if cur.right:
                    q.append(cur.right)
                    check.append(1)
                else:
                    check.append(0)
                
                #should be all full unless the last level
            
            all_check.append(check)
            
        return validate(all_check[:-1])
