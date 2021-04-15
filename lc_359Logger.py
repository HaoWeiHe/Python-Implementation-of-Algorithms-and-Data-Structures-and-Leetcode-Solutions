class Logger(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.h = {}

    def shouldPrintMessage(self, t, message):
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        :type timestamp: int
        :type message: str
        :rtype: bool
        """
        if message not in self.h:
            self.h[message] = t
        else:
            if self.h[message]  + 10 > t:
                return False
            self.h[message] = t
        return True
        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)