class SnapshotArray(object):
    """
    0 : {0:1}
    1 : {0,2}
    """
    def __init__(self, length):
        """
        :type length: int
        """
        self.d = collections.defaultdict(dict)
        self.snapid = 0 

    def set(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        
        self.d[self.snapid][index] = val
       
    def snap(self):
        """
        :rtype: int
        """
        
        self.snapid += 1
        self.d[self.snapid] = {k:v for k,v in self.d[self.snapid-1].items()}
        
        return self.snapid -1
    def get(self, index, snap_id):
        """
        :type index: int
        :type snap_id: int
        :rtype: int
        """
        # for i in range(snap_id, -1, -1):
        #     if index in self.d[i]:
  
        if index in self.d[snap_id]:
            return self.d[snap_id][index] 
        return 0


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)