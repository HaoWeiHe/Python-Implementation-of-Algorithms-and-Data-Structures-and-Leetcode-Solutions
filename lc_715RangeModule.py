"""
10,20
10 14
16 20 
"""
class RangeModule(object):

    def __init__(self):
        self.rgns = []

    def addRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: None
        """
        # 8,9
        # 1,8
        effect = []
        new_pair = (left, right)


        for e in self.rgns:
            if e[0] > right or e[1] < left :
                continue
            effect.append(e)
            new_pair = (min(new_pair[0],e[0]), max(new_pair[1], e[1]))
        for e in effect:
            self.rgns.remove(e)
        self.rgns.append(new_pair)
        

    def queryRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: bool
        """
        
        for e in self.rgns:
            if e[0] <= left and  e[1]>= right :
                return True
        
        return False

    def removeRange(self, left, right):
        rmv = []
        insrt = []
        for e in self.rgns:
            if e[0] > right or e[1] < left : 
                continue
            if e[0] < left and e[1] >= right:
                rmv.append(e)
                insrt.append((e[0], left))
                insrt.append((right, e[1]))
            elif left <= e[0] and right >= e[1]:
                rmv.append(e)
            elif e[0] < left and e[1] < right:
                rmv.append(e)
                insrt.append((e[0],left))
            elif e[0] > left and e[1] > right:
                rmv.append(e)
                insrt.append((right,e[1]))
        for e in rmv:
            self.rgns.remove(e)
        self.rgns+= insrt
 
# 1) case 1
# [-----)
# 10    20
#   (|-|]
# split A into 2 time zone
# 2) case 2
#   |--|
# |======|
# [      )
#  remove A
# 3) case 3:
#   |------|
#     |=======|
#     (       )
#   update A.end into remv.start
# 4) case 4:
#   |------|
# |===|    
# ()
#   update A.end into remv.end

# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)