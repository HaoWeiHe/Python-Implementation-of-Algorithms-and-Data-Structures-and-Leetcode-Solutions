
class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        [[1,1],2,[1,1]]
         [dfs(e) + 2 + dfs(e) for e in Lst]
        """
        # self.lst = nestedList
        def dfs(r):
           
            for e in r:
                if e.isInteger():
                    yield e.getInteger()
                else:
                    for e in dfs(e.getList()):
                        yield e
        self.g = dfs(nestedList)
        self.nxt = None

    def next(self):
        """
        :rtype: int
        """
        return self.nxt

    def hasNext(self):
        """
        :rtype: bool
        """
        try:
            self.nxt = next(self.g)
            return True
        except:
            return False

