from heapq import heappop as pop, heappush as push
class TimeMap(object):
    """
    1.heapq
    2. double linkedin list + search the bondary
     
    """
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.ts = [] #[(t, key, val)]
        

    def set(self, k, v, t):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        push(self.ts,(t,k,v))
        

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        ans = ""
        poped_lst = []
        while self.ts:
            t,k,v = pop(self.ts)
            poped_lst.append((t,k,v))
            if t > timestamp:
                break
            if k == key:
                ans = v
        while poped_lst:
            push(self.ts,poped_lst.pop())
        return ans
                
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)