class SnapshotArray(object):

    def __init__(self, length):
       
        
        self.lst = [0] * length
        self.shot = []
        self.buf = defaultdict()

    def set(self, index, val):
        
        self.lst[index] = val
        self.buf[index] = val
        
    def snap(self):
        dup = {}
        for k in self.buf:
            dup[k] = self.buf[k]
        self.shot.append(dup)
        return len(self.shot) -1

    def get(self, index, snap_id):
        
        if snap_id == len(self.shot):
            return self.lst[index]
      
        if index in self.shot[snap_id]:
            return self.shot[snap_id][index]
        
        return 0


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)