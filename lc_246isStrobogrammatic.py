class Solution(object):
    def isStrobogrammatic(self, num):
        """
        "6969"
          ^
           69
         96 and rotate == 69
        6-> 9
        9-> 6
        
        """
        d = {"6":"9", "8":"8","0":"0", "1":"1","9":"6"}
        for i in range(1,11):
            if str(i) not in d:
                d[str(i)] = "#"
        for i in range(len(num)):
            if num[i]!= d[num[~i]]:
                return False
        return True
        