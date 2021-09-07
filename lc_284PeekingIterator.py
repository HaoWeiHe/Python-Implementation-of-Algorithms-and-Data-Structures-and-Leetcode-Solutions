

class PeekingIterator:
    def __init__(self, iterator):
        """
        #if peak, append to buf:
        #everytime next, check buf
        ---
        hasNext == False : no hasNext and buf is empty
        """
        self.buf = deque([])
        self._iter = iterator
        

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if self.buf:
            return self.buf[0]
        
        ele = self._iter.next()
        self.buf.append(ele)
        return ele
        

    def next(self):
        """
        :rtype: int
        """
        if self.buf:
            return self.buf.popleft()
        return self._iter.next()
        

    def hasNext(self):
        """
        :rtype: bool
        """
        if not self.buf and self._iter.hasNext() == False:
            return False
        return True

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].