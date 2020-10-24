
# class LRUCache(object):

#     def __init__(self, capacity):
#         self.cache = collections.OrderedDict()
#         self.capacity = capacity
    
#     #first one is the oldest one
    
#     def get(self, key):
#         if key in self.cache:
#             self.cache.update(key)
#             return self.cache[key]
#         return -1
    
#     def put(self,key, value):
#         """
       
#         put d[key] = value
#         d[key] move to end
#         if size > cap: 
#             eviction the last one
        
#         """
        
#         self.cache[key] = value
#         self.cache.update(key)
#         if len(self.cache) > self.capacity:
#             self.cache.popitem(last =False)

# 1. double-linkedlist:
#     A/ka - B/kb - C/kc - D/kd
# 2. hashmap 
# {A:"Obj_A",B:"Obj_B",C:"Obj_C"}

# init: head, tail

# class LRUCache(object):

#     def __init__(self, capacity):
#         self.cache = collections.OrderedDict()
#         self.capacity = capacity
    
#     #first one is the oldest one
    
#     def get(self, key):
#         if key in self.cache:
#             self.cache.update(key)
#             return self.cache[key]
#         return -1
    
#     def put(self,key, value):
#         """
       
#         put d[key] = value
#         d[key] move to end
#         if size > cap: 
#             eviction the last one
        
#         """
        
#         self.cache[key] = value
#         self.cache.update(key)
#         if len(self.cache) > self.capacity:
#             self.cache.popitem(last =False)

# 1. double-linkedlist:
#     A/ka - B/kb - C/kc - D/kd
# 2. hashmap 
# {A:"Obj_A",B:"Obj_B",C:"Obj_C"}

# init: head, tail

class LinkedLst():
    def __init__(self):
        self.prev  = None
        self.nxt = None
        self.key = 0
        self.val = 0
        
class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.head = LinkedLst()
        self.tail = LinkedLst()
        self.capacity = capacity
        self.cache = {}
        self.head.nxt = self.tail
        self.tail.prev = self.head
        
    def update(self,node):
        # AbCD<-tail
        # ACDb
        node.nxt.prev = node.prev
        node.prev.nxt = node.nxt
        self.add_new(node)
        
    def add_new(self, node):
        #ABCD 
        old_tailnode = self.tail.prev
        old_tailnode.nxt = node
        node.prev = old_tailnode
        node.nxt = self.tail
        self.tail.prev = node
    
    def remove_first(self):
        # head->A B CD
        # head -> B
        ori_first = self.head.nxt
        self.head.nxt = self.head.nxt.nxt
        self.head.nxt.prev = self.head
        return ori_first.key
    
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.cache:
            node = self.cache[key]
            self.update(node)
            return node.val
        
        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            update(node)
        else:
            node = LinkedLst()
            node.val = value
            node.key = key
            self.cache[key] = node
            self.add_new(node)
            # print(self.cache,self.cache[1].key,self.cache[1].value)
            
        if len(self.cache) > self.capacity:
            ori_first = self.remove_first()
            del self.cache[ori_first]
        
       
# ["LRUCache","put","put","get","put","get","put","get","get","get"]
# [[2]        ,[1,1],[2,2],[1],[3,3],  [2],[4,4],[1],[3],[4]]
# [null,       null,  null,1,  null,    -1 ,null,1,-1,-1]