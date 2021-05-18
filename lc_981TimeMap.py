class Node():
    def __init__(self,k,v,t):
        self.prev = None
        self.next = None
        self.val = v
        self.key = k
        self.time  = t 
        
class LinkedList():
    def __init__(self):
        self.head =  Node(None,None, -1)
        self.tail = Node(Node,None, 10**7 + 1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.head.prev = None
        self.tail.next = None
        self.minT = None
        self.maxT = None

class TimeMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.lst = LinkedList()
        

    def set(self, key, value, timestamp):
        """
            A  B - C
              v
            tmp = B
            A.next = new
            new.pre = A
            v.next = tmp
            tmp.prev = V
        
        A B C tail
         ^
        """

        cur = self.lst.tail
        while cur :
            if cur.time < timestamp: #insert behind this #cur = A
                tmp = cur.next
                new = Node(key,value, timestamp)
                cur.next = new
                new.prev = cur
                new.next = tmp
                tmp.prev = new
                break
            cur= cur.prev
        
        

    def get(self, key, timestamp):
        """
        A B C 
          v
          start here
        """
        cur = self.lst.tail
        while cur and cur.time > timestamp:
            
            cur = cur.prev
        while cur:
            if cur.key == key:
                return cur.val
            cur = cur.prev
        return ""
            
            
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)