#binary search with defulatdict[list]
class TimeMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = defaultdict(list)
        

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        self.d[key].append((value, timestamp))

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        lst = self.d[key]    
        l, r = 0, len(lst)
        while l < r:
            m = (l+r)/2
            if self.d[key][m][1] >timestamp:
                r = m
            else:
                l = m + 1
        
        if r == 0:
            return ""
        return self.d[key][l-1][0]

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)