"""
t1 -> idx 1
t2 -> idx 2


"""

class LogSystem(object):

    def __init__(self):
        self.d = {}
        self.getid = {"Year":0, "Month":1,"Day":2,"Hour":3,"Minute":4,"Second":5}
    
    def put(self, id, t):
        """
        :type id: int
        :type timestamp: str
        :rtype: None
        """
        self.d[tuple(t.split(":"))] = id
        
    
    def retrieve(self, start, end, granularity):
        """
        ["2017:01:01:23:59:58","2017:01:02:23:59:58","Second"]]
                   ^
        """
        ans = []
        qid = self.getid[granularity]
        start, end = tuple(start.split(":")[:qid + 1]), tuple(end.split(":")[:qid + 1])
        for time, i in self.d.items():
            if start <= time[:qid + 1] <=  end:
                ans.append(i)
        return ans


# Your LogSystem object will be instantiated and called as such:
# obj = LogSystem()
# obj.put(id,timestamp)
# param_2 = obj.retrieve(start,end,granularity)