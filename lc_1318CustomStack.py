class CustomStack(object):

    def __init__(self, maxSize):
        """
        :type maxSize: int
        """
        self.sz = maxSize;
        self.stk = []
    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if len(self.stk) < self.sz:
            self.stk.append(x)
    def pop(self):
        """
        :rtype: int
        """

        if not self.stk:
            return -1
        return self.stk.pop()

    def increment(self, k, val):
        """
        :type k: int
        :type val: int
        :rtype: None
        """

        for i in range(min(k, len(self.stk))):
            self.stk[i] += val
