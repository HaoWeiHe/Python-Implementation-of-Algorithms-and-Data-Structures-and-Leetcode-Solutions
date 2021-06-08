"""
[1,2,3]
Q pop: 1
S pop:3
counter = 0 
[] [1,2] if len(q1)==1: pop else, pop and push to another
push: 
if counter ==0:
push to A
return
if not A:
push to A
else:
push to B
pop:
pop the one has val 

counter -= 1
top:
empty:
return counter ==0
"""
class MyStack(object):

    def __init__(self):
        self.c = 0 
        self.q1 = deque([])
        self.q2 = deque([])

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: None
        """
        self.c += 1 
        if self.c == 1:
            self.q1.append(x)

            return 
        if self.q1:
            self.q1.append(x)
            
        if self.q2:
            self.q2.append(x)
        

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        if self.c == 0:
            return None
        
        self.c -= 1
        def helper(q1, q2):
            top = None
            while q1:
                top = q1.popleft()
                if q1:
                    q2.append(top)
            return top
            
        if self.q1:
            return helper(self.q1, self.q2)
        
        if self.q2:
            return helper(self.q2, self.q1)
            

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        if self.q1:
            return self.q1[-1]
        if self.q2:
            return self.q2[-1]
        return None
        

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return self.c == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()