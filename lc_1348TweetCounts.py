"""
tweet3 0
tweet3 60
tweet3 10
-> tweet3: [0,10,60] -> use O(n) or O(logn) but have extrac space
0, 60, tweet3, min
use min: idx: 0/60 -> 0 
        600 /60-> 10
#append to 10, and idx[10] + 1        
or we can use maxheap and leverage it to init our list for ans


"""

class TweetCounts(object):

    def __init__(self):
        
        self.d = defaultdict(list)
        self.scale = {"minute": 60, "hour":3600, "day":86400}

    def recordTweet(self, tweetName, time):
        """
        :type tweetName: str
        :type time: int
        :rtype: None
        """
        self.d[tweetName].append(time)
        
        
        
    def getTweetCountsPerFrequency(self, freq, tweetName, startTime, endTime):
        """
        :type freq: str
        :type tweetName: str
        :type startTime: int
        :type endTime: int
        :rtype: List[int]
        """
        
        denominator = self.scale[freq]
        ans = [0]* (1+(endTime-startTime)/denominator)
        
        for f in self.d[tweetName]:
            
            if startTime <= f <= endTime:
                idx =  (f-startTime)/denominator 
                ans[idx] += 1
           
        return ans
            


# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)