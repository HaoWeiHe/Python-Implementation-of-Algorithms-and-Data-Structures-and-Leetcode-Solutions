class Solution(object):
    def countBits(self,nums):


        res = []
        res.append(0)

        for i in range(1,nums+1):

            if i%2==0:
                res.append(res[i/2])
            else:
                res.append(res[i/2]+1)

        return res