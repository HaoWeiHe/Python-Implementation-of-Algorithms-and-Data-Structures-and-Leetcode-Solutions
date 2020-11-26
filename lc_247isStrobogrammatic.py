class Solution(object):
    def isStrobogrammatic(self, num):
        """
        nums look the same when 180 rotated: 0,1,8,69,96
        """
        revise = {"6":"9","9":"6","0":"0","8":"8","1":"1"}
        l,r  = 0, len(num)-1
        while l <=r:
            c1, c2 = num[l], num[r]
            if c1 in revise and c2 in revise and revise[c1] == c2:
                l +=1
                r -=1
            else:
                return False
        return True