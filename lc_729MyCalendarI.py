class MyCalendar(object):

    def __init__(self):
        self.l = []

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
       
        for e in self.l:
            s,e = e
            if s <= start < e or  s < end < e or start <= s < end or start < e < end:
                return False
        
        self.l.append([start, end])
        return True
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)