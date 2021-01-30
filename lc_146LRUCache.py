class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.d = collections.OrderedDict()
        self.c = capacity
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.d:
            self.d.move_to_end(key)
            return self.d[key]
        return -1
    
    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
      
        self.d[key] = value
        self.d.move_to_end(key)
        
        if len(self.d) > self.c:
            self.d.popitem(last = False)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)