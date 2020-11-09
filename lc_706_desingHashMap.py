class Busket():
    def __init__(self):
        self.busket = []
        
    def get(self,key):
        for k, v in self.busket:
            if k == key:
                return v
        return -1
    
    def insert(self,key, value):
        exist = False
        for i, cell in enumerate(self.busket):
            cell_k, cell_v = cell
            if key == cell_k:
                self.busket[i] = (key,value)
                exist = True
                break
        if not exist:
            self.busket.append((key,value))
            
        
    def remove(self,key):
        for i, cell in enumerate(self.busket):
            cell_k, cell_v = cell
            if key == cell_k:
                del self.busket[i]
        
class MyHashMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.key_space = 2069
        self.hashtable  = [Busket() for _ in range(self.key_space)]

    def put(self, key, value):
        hash_key = key % self.key_space
        self.hashtable[hash_key].insert(key,value)
        

    def get(self, key):
        hash_key = key % self.key_space
        return self.hashtable[hash_key].get(key)
    
    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: None
        """
        hash_key = key % self.key_space
        self.hashtable[hash_key].remove(key)
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
# class MyHashMap(object):

#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.hash = {}

#     def put(self, key, value):
#         """
#         value will always be non-negative.
#         :type key: int
#         :type value: int
#         :rtype: None
#         """
#         self.hash[key] = value
        

#     def get(self, key):
#         """
#         Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
#         :type key: int
#         :rtype: int
#         """
        
#         return self.hash.get(key,-1)

#     def remove(self, key):
#         """
#         Removes the mapping of the specified value key if this map contains a mapping for the key
#         :type key: int
#         :rtype: None
#         """
#         if key in self.hash:
#             del self.hash[key]
        


# # Your MyHashMap object will be instantiated and called as such:
# # obj = MyHashMap()
# # obj.put(key,value)
# # param_2 = obj.get(key)
# # obj.remove(key)
