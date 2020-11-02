"""

1) linkedlst
head                        tail
[Obj1] - [Obj2] - [Obj3] -[Obj4]
Max      freq: 3   freq:1, set = ["hello"]
         set = ["leetcode", "hey"]


2) hashtable {string: object_number}
{"leetcode": object1, "hello": object2} 

dec:
1) if string not exist: 
    return 

2) if string exist:
    if len(node's list) ==1:
        remove node
        (obj.left.right = obj.right & obj.right.left = obj.left)
    else:
        remove string from node's list
        (obj.string_set.remove(string) #remove from lst)

    2.1 if freq(string) ==1: del hashtable[string] 
        #remove  tring from hashtable

    2.2 if freq(string) >1:
        if node.left.freq == freq -1: append
        else: create a new node, and insert
        update the hashtable!   

inc:
    1) if string not exist: 
        if freq == 1 exist: append
        if freq == 1 not exist: create new one on the right of tail
    2) if string exsit:
        
        2.1  freq +1 exist 
            append string to node
        2.2 freq +1 not exist
            insert node on the obj.left
        update hashtable

"""

# ["AllOne","inc","inc","inc","inc","inc","dec","getMaxKey","getMinKey"]
# [[],["hello"],["hello"],["world"],["world"],["hello"],["world"],[],[]]

class linkedlst():
    def __init__(self):
        self.right = None
        self.left = None
        self.freq = 0
        self.strings = set()


class AllOne(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = linkedlst()
        self.tail = linkedlst()
        self.hashtable = {}
        self.head.right = self.tail
        self.tail.left = self.head


    def remove_node(self, node):
        # node.left node node.right
        #
        node.right.left = node.left
        node.left.right = node.right

    def inc(self, key):
        """
        1) if string not exist: 
            if freq == 1 exist: append
            if freq == 1 not exist: create new one on the right of tail
        2) if string exsit:
            
            2.1  freq +1 exist 
                append string to node
            2.2 freq +1 not exist
                insert node on the obj.left
            update hashtable
        """
        node = self.hashtable.get(key)
#head - tail
#head - newNode - tail
        if not node:
            if self.tail.left.freq == 1:
                self.tail.left.strings.add(key)
                self.hashtable[key] = self.tail.left
            else:
                newNode = linkedlst()
                newNode.left = self.tail.left
                newNode.right = self.tail
                newNode.left.right = newNode
                self.tail.left = newNode
                newNode.freq = 1
                newNode.strings.add(key)
                self.hashtable[key] = newNode
        if node:
            freq_of_key = node.freq
            node.strings.remove(key)

            if node.left != self.head and node.left.freq == freq_of_key + 1:
                node.left.strings.add(key)
                self.hashtable[key] = node.left
            else:
                newNode = linkedlst()
                newNode.right = node
                newNode.left = node.left
                newNode.left.right = newNode
                node.left = newNode
                newNode.freq = freq_of_key +1
                newNode.strings.add(key)
                self.hashtable[key] = newNode

            if len(node.strings) ==0:
                self.remove_node(node)

        
    def dec(self, key):

        """
        1) if string not exist: 
            return 

        2) if string exist:
            if len(node's list) ==1:
                remove node
                (obj.left.right = obj.right & obj.right.left = obj.left)
            else:
                remove string from node's list
                (obj.string_set.remove(string) #remove from lst)

            2.1 if freq(string) ==1: del hashtable[string] 
                #remove  tring from hashtable

            2.2 if freq(string) >1:
                if node.right.freq == freq -1: append
                else: create a new node, and insert
                update the hashtable!   
        """
        node = self.hashtable.get(key)
        if not node:  
            return 

        freq_of_key = node.freq
        node.strings.remove(key)

        
        if freq_of_key == 1:
            del self.hashtable[key]
        else:
            if node.right != self.tail and node.right.freq == freq_of_key -1:
                node.right.strings.add(key)
                self.hashtable[key] = node.right
            else:
                newNode = linkedlst()
                newNode.right = node.right
                node.right.left = newNode
                newNode.left = node
                node.right = newNode
                newNode.strings.add(key)
                newNode.freq = freq_of_key -1
                self.hashtable[key] = newNode

        if len(node.strings)  == 0:
           self.remove_node(node)
        

    def getMaxKey(self):
    
        if self.head.right != self.tail:
            ele = self.head.right.strings.pop()
            self.head.right.strings.add(ele)
            return ele

        return ""
        

    def getMinKey(self):
        

        if self.tail.left != self.head :#and self.tail.right:
            
            ele = self.tail.left.strings.pop()
            self.tail.left.strings.add(ele)

            return ele
        return ""


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()