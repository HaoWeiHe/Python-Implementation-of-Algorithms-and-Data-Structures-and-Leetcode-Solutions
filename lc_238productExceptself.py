
class Solution(object):
    def productExceptSelf(self, lst):
        #lst = [1,2,3,4]
        n = len(lst)
        res = [1]
        for idx in range(1,n):
            res.append(res[idx-1] * lst[idx-1])
        R = 1
        for idx in range(n-1,-1,-1):
            res[idx] = R * res[idx]
            R *= lst[idx]
        return res
        
    # def productExceptSelf1(self, lst):
    #     """
    #     :type nums: List[int]
    #     :rtype: List[int]
    #     """
    #     if not lst:
    #         return 0
    #     rt_product = [1 for _ in lst]
    #     lf_product = [1 for _ in lst]

    #     n  = len(lst)
    #     for idx in range(1,n):
    #         rt_product[idx] = rt_product[idx-1] * lst[idx -1]

    #     for idx in range(n-2,-1,-1):
    #         lf_product[idx] = lf_product[idx+1] * lst[idx+1]
       
    #     return [ rt_product[i] * lf_product[i] for i in range(n)]

