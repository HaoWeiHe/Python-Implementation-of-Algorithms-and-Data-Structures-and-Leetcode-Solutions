class Solution(object):
    def carFleet(self, target, position, speed):
        paris = zip(position,speed)
        #[8,3,7,1,1]
        #if pre is need more time, it become the new lead
        ts = [ float(target-p)/s for p,s in sorted(paris)]
     
        ans = 0
        lead = 0
        for t in ts[::-1]:
            if t > lead:
                lead = t
                ans +=1
        return ans
