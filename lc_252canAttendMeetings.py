class Solution(object):
    def canAttendMeetings(self, its):
        """
        :type intervals: List[List[int]]
        :rtype: bool
         [[2,4] [7,10]]
        """
        if not its:return True
        its.sort(key = lambda x: (x[0],x[1]))
        
        pre = its[0][1]
        for ele in its[1:]:
            if ele[0] < pre: return False
            pre = ele[1]
        return True