class Node(object):
    def __init__(self,key = None, value = None):
        self.prev = None
        self.next = None
        self.key = key
        self.value = value


class LRUCache(object):


    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.d = {}#key: node_obj
        self.c = capacity
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def move_to_end(self, key):
        value = self.d[key].value
        self.remove(key)
        self.add_node(key,value)

    def remove(self,key):
        node = self.d[key]
        node.prev.next = node.next
        node.next.prev = node.prev
        del self.d[key]

    def pop_frist(self):
        first_key = self.head.next.key
        self.head.next = self.head.next.next
        self.head.next.prev = self.head
        del self.d[first_key]

    def add_node(self, key,val):
        new_node = Node(key = key, value = val)
        ori_tail = self.tail.prev
        new_node.next = self.tail
        self.tail.prev = new_node
        new_node.prev = ori_tail
        ori_tail.next = new_node
        self.d[key] = new_node

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.d:
            self.move_to_end(key)
            return self.d[key].value
        return -1
    
    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        # if key in self.d:
        #     self.d[key].value = value
        # else:
        if key in self.d:
            self.remove(key)
        self.add_node(key,value)
        
        if len(self.d) > self.c:
            self.pop_frist()


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)