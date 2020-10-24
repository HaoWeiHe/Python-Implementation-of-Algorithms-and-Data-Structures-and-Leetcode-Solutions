from collections import OrderedDict
class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = OrderedDict()
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.cache:
            self.cache.move_to_end(key,last= False)
            return self.cache[key]
        else:
            return -1
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        self.cache.update({key:value})
        self.cache.move_to_end(key, last=False)

        if (len(self.cache)) > self.capacity:
            self.cache.popitem()



# [null,null,null,1,null,2,null,-1,3,4]
# Expected answer
# [null,null,null,1,null,-1,null,-1,3,4]