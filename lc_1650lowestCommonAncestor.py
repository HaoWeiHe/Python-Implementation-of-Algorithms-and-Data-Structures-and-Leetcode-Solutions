
class Solution(object):
    def lowestCommonAncestor(self, a, b):
        """
        :type node: Node
        :rtype: Node
        """
        p1, p2 = a, b
        while p1!= p2:
            p1 = p1.parent if p1.parent else b
            p2 = p2.parent if p2.parent else a
        return p1
        
        