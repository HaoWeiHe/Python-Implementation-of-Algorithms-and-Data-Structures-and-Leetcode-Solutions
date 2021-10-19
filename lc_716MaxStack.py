class MaxStack(object):

    def __init__(self):
        self.s = []
        self.mx = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.s.append(x)
        tmp = x if not self.mx else max(self.mx[-1], x)
        self.mx.append(tmp)
        

    def pop(self):
        """
        :rtype: int
        """
        ele = self.s.pop()
        self.mx.pop()
        return ele

    def top(self):
        """
        :rtype: int
        """
        return self.s[-1]
        

    def peekMax(self):
        """
        :rtype: int
        """
        return self.mx[-1]

    def popMax(self):
        """
        :rtype: int
        """
        tmp_max = self.mx[-1]
        can  =[]
        while self.s:
            ele = self.s.pop()
            self.mx.pop()
            if ele == tmp_max:
                break
            can.append(ele)
        while can:
         
            ele = can.pop()
            self.push(ele)
        return tmp_max
            


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()