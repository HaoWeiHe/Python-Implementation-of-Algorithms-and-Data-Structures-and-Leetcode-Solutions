"""
    [[1,1],2,[1,1]]
    [[2],2,[2]]
"""
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution(object):
    def depthSumInverse(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        maxD = 0
        def dfs(lst):
            if not lst:
                return 0
            
            ans = 1
            for e in lst:
                if e.getInteger():
                    ans = max(ans, dfs(None)+1)
                else:
                    ans = max(ans, dfs(e.getList())+1 )
                    
            return ans
        maxD = dfs(nestedList)
        self.res = 0 
        def dfs(lst, d):

            for e in lst:
                val = e.getInteger()
                if val:
                    self.res+= val *(maxD - d +1)
                else:
                    dfs(e.getList(), d+1)
        
        dfs(nestedList, 1)
        return self.res
                    
                    
        