class MinStack(object):

    def __init__(self):
        """
       [2,5,1,9]
       [2] min:[2,]
       [2,5] min:[2,2]
       [2,5,1] min [2,2,1]
       [2,5,1,9] min [2,2,1,1]
     
        """
        self.q = []
        self.m = []
        self.counter = 0 
        

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.counter += 1
        self.q.append(val)
        if self.m:
            if (self.m[-1][0]) > val:
                self.m.append((val, self.counter))
        else:
            self.m.append((val, self.counter))
        

    def pop(self):
        """
        :rtype: None
        """
        self.counter -= 1
        ans = self.q.pop()
        if self.m[-1][1] > self.counter:
            self.m.pop()
            
        return ans 

    def top(self):
        """
        :rtype: int
        """
        return self.q[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.m[-1][0]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()