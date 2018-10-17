class MinStack(object):
    
    
    def __init__(self):
        self.stack = list()
        self.stack2 = list()
        
    def push(self, x):
        
        self.stack.append(x)
        
        if len(self.stack2) == 0:
            self.stack2.append(x)
        else:
            if x <= self.stack2[-1]:
                self.stack2.append(x)

    def pop(self):
        
        s = self.stack.pop()
        
        if len(self.stack2) > 0:
            if s == self.stack2[-1]:
                self.stack2.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        if len(self.stack2) == 0:
            return []
        return self.stack2[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()