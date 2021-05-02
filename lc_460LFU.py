class Node():
    def __init__(self,key, value):
        self.val = value
        self.key = key
        self.freq = 1


class LFUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.D ={}
        self.capacity = capacity
        self.F = defaultdict(OrderedDict)
        self.minF = 0 


    def get(self, key):
        """
        *query by calling D
        if not exist return -1
        orifreq + 1
        append curnode in to F[newfreq]
        remove key from D[orifreq], if empty, minF++
        return D[key].val
        """
        if key not in self.D:
            return -1
        cur_node = self.D[key]
        
        orif = cur_node.freq
        self.D[key].freq += 1
        
        self.F[orif+1][key] = cur_node

        del self.F[orif][key]
        if not self.F[orif] and self.minF ==  orif :
            self.minF += 1
        return self.D[key].val
        

    def put(self, key, value):
        """
        if already exist:
            change value 
            call get(key) 
        else:
            if cap is full (len(D) == C): evict the firstNode, foo, in D[minF]  and remove foo from D
            create new node
            minF = 1
            F[1] = {newkey, newNode}
            D[key] = newvalue
            
        """
        if self.capacity == 0:return
        if key in self.D:
            self.D[key].val = value
            self.get(key)
            return 
       
        if len(self.D) == self.capacity:
            k, n = self.F[self.minF].popitem(last=False)
            del self.D[k]
        newNode = Node(key, value)
        self.minF = 1
        self.D[key] = newNode
        self.F[1][key] = newNode
        
        
# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)