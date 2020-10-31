class Solution(object):
    def multiply(self, num1, num2):
        """
                11
        num1 = "123"
                012+1
        num2 = "456"
        ----------------
res =  [0,0,0,1,1,0]
car =             8 (18+0)/10
rem =         6  3  8(18+0)%10

divmod(num1[i]*num2[j] + res[i+j])
-------------------------------
        [0,0,0,6,3,8]
        """
        res =[0] * (len(num1) + len(num2))

        
        for j in range(len(num2)-1,-1,-1):
            for i in range(len(num1)-1,-1,-1):
                car, rem = divmod(int(num1[i])* int(num2[j]) + res[i+j+1],10)
                res[i+j+1] = rem
                res[i+j] += car
                rem, car = 0,0
        while res:
            if res[0] ==0: 
                res.pop(0)
            else: 
                break
        return "".join(map(str,res)) if res else "0"





num1, num2 = "123","456"
print(Solution().multiply(num1,num2))