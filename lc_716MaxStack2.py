"""
heap and linkedinlist
[val:obj]  obj.prev, obj.next



"""
class Node(object):
    def __init__(self, val = None):
        self.val = val
        self.next = None
        self.prev = None

class DLL(object):
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

from heapq import heappush, heappop
class MaxStack(object):

    def __init__(self):
        self.heap = []
        self.dll = DLL()
        self.d = defaultdict(list)
    def push(self, x):
        """
            hpush, 
            ori_tail = tail.prev
            ori_tail.next =obj
            obj.prev = ori_tail
            obj.next = tail
            tail.prev = obj
        """
        node = Node(x)
        heappush(self.heap,[-x, node])
        ori_tail = self.dll.tail.prev
        ori_tail.next = node
        node.prev = ori_tail
        node.next = self.dll.tail
        self.dll.tail.prev = node
        self.d[x].append(node)

    def pop(self):
        
        """
        remove_node = tail.prev
        and find this node in heap and remove!

        tail.prev = tail.prev.prev
        tail.prev.next = tail

        """
        remove_node = self.dll.tail.prev
        can = []
        while self.heap:
            val, obj = heappop(self.heap)
            if obj == remove_node:
                break
            can.append([val,obj])
        while can:
            heappush(self.heap, can.pop())
        self.dll.tail.prev = remove_node.prev
        remove_node.prev.next = self.dll.tail
        self.d[remove_node.val].pop()
        return remove_node.val

    def top(self):
        """
        return tail.prev.val
        """
        return self.dll.tail.prev.val
        

    def peekMax(self):
        """
        peekMax:
        return h[-1]
        """
        return -self.heap[0][0]
        

    def popMax(self):
        """

            popMax:
                obj = h.pop()
                
                obj.prev.next = obj.next
                obj.next.prev = obj.prev
        """
        x = -self.heap[0][0]
        target = self.d[x].pop()
        can = []
        while self.heap:
            val, obj = heappop(self.heap)
            if obj == target:
                break
            can.append([val,obj])
        while can:
            heappush(self.heap,can.pop())
        
        target.prev.next = target.next
        target.next.prev = target.prev
        return target.val
