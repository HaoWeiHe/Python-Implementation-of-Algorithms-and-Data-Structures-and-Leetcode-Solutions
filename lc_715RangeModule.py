"""
10,20
10 14
16 20 
"""
class RangeModule(object):

    def __init__(self):
        self.lst = []

    def addRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: None
        """
        inserted = 0
        ans = []
        for e in self.lst:
            if e[0] > right and inserted == 0:
                inserted =1
                ans.append([left,right])
            if e[1] < left or e[0] > right:
                ans.append(e)
            else:
                left, right = min(left, e[0]), max(right, e[1])
        if inserted == 0 :
            ans.append([left, right])
        self.lst = ans
        
        # 8,9
        # 1,8
        # effect = []
        # new_pair = (left, right)


        # for e in self.lst:
        #     if e[0] > right or e[1] < left :
        #         continue
        #     effect.append(e)
        #     new_pair = (min(new_pair[0],e[0]), max(new_pair[1], e[1]))
        # for e in effect:
        #     self.lst.remove(e)
        # self.lst.append(new_pair)
        

    def queryRange(self, left, right):
    
        l, r = 0, len(self.lst) - 1
        while l <= r:
            m = (l+r)/2
            if self.lst[m][1] < left:
                l = m + 1
            elif self.lst[m][0] > right:
                r = m -1
            else:
                return self.lst[m][0] <= left and self.lst[m][1] >= right
        return False

        # for e in self.lst:
        #     if e[0] <= left and  e[1]>= right :
        #         return True
        
        # return False

    def removeRange(self, left, right):
    
        ans = []
        for e in self.lst:
            if e[1] <= left or e[0] >= right:
                ans.append(e)
            else:
                """
                left-----right
            e--------e
            e----------------------e
                        e---e
                        e------------e
                """
                if e[0] < left:
                    ans.append([e[0], left])
                if e[1] > right:
                    ans.append([right, e[1]])
        self.lst = ans
# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)
class RangeModule2(object):

    def __init__(self):
        self.l = []
    def addRange(self, left, right):
        """
        [(1,3),(5,7),(100,1002)] ins(2,8)
        new (1,8)
        new (2,8)
        
        lst = [(100,1002)]
        """
        tmp = []
        inserted  = False
        new_pair = (left,right)
        for i,e in enumerate(self.l):
            start, end = e[0], e[1]
           
            if right < start or left > end:
                
                if inserted:
                    tmp.append(new_pair)
                    tmp += self.l[i:]
                    break
                tmp.append(e)
                continue
            inserted = True
            
            new_pair = (min(new_pair[0], left), max(new_pair[1], right))
        if inserted  == False:
            tmp.append(new_pair)
       
        self.l = tmp[:]
    def queryRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: bool
        """
        
        
        # queryRange(10, 14): true (Every number in [10 left, 14 right) is being tracked)
        for e in self.l:
            if e[0] <= left and  e[1]>= right :
                return True
        
        return False
        

    def removeRange(self, left, right):
        rmv = []
        insrt = []
        for e in self.l:
            """
                 |==============|
        right    e0              e1  left
                10              14   14,18
            """
            if right < e[0] or e[1] <= left : 
                continue

            # 2) case 2
            #   |--|
            # |======|
            # [      )                    
            if left <= e[0] and right >= e[1]:
                rmv.append(e)
            # 1) case 1
                # [-----)
                # 10    20
                #   (|-|]
                # split A into 2 time zone
            elif e[0] <= left and e[1] >= right:
                rmv.append(e)
                if e[0]!= left:
                    insrt.append((e[0], left))
                if e[1]!=right:
                    insrt.append((right, e[1]))
            # 3) case 3:
            #   |------|
            #     |=======|
            #     (       )
            elif e[0] < left and e[1] < right:
                rmv.append(e)
                insrt.append((e[0],left))
            # 4) case 4:
            #  e0|------|e1
            # |=====|  right
            # ()
            elif e[0] > left and e[1] > right:
                rmv.append(e)
                insrt.append((right,e[1]))
        for e in rmv:
            self.l.remove(e)
        self.l+= insrt
 
