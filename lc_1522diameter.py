"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution(object):
    def diameter(self, root):
        """
        :type root: 'Node'
        :rtype: int
        """
        self.res = 0 
        def dfs(root):
            if not root:return 0
            #return the max_diameter path : 1 + max(all_childre)
            #tmp_max_diameter = pick_up_max_two_nodes(all_children)
            max_diameter, q = 0, []

            for c in root.children:
                c_res = dfs(c)
                heapq.heappush(q, c_res)
                if len(q) > 2:
                    heapq.heappop(q)
                max_diameter = max(max_diameter, c_res)
           
            self.res = max(self.res, sum(q)) #compare the number of edges
            return 1 + max_diameter

        dfs(root)
        return self.res #return the number of nodes
            
            