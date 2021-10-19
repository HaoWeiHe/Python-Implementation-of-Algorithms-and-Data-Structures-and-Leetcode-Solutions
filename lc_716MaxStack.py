from heapq import heappush as hpush, heappop as hpop


class MaxStack(object):

    def __init__(self):
        self.h = []
        self.stack = []

    def push(self, x):
        hpush(self.h, -x)
        self.stack.append(x)
        
    def pop(self):
        """
        :rtype: int
        """
        top = self.stack.pop()
        can = []
        while self.h:
            ele = hpop(self.h)
            if ele == -top:
                break
            can.append(ele)
        for ele in can:
            hpush(self.h, ele)
        
        return top

    def top(self):
        return self.stack[-1]

    def peekMax(self):
        return -self.h[0]
        

    def popMax(self):
        """
        :rtype: int
        """
        top = hpop(self.h)
        q = []
        while self.stack:
            cur = self.stack.pop()
            if cur == -top:
                break
            q.append(cur)
        while q:
            self.stack.append(q.pop())
        return -top


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()