class Solution(object):
    def multiply(self, num1, num2):
        """
                11
        num1 = "123"
        num2 = "456"
                738
                15
        res = [ 738]
        car = [ ]
        
        """
        if num1=="0" or num2=='0': return "0"
        num1 = num1[::-1]
        num2 = num2[::-1]
        final_car = 0
        car,rem, res = 0,0,[0 for x in range(len(num2)+len(num1)) ]
        for i in range(len(num1)):
            for j in range(len(num2)) :
                
                _sum = int(num1[i]) * int(num2[j])
                car, rem = divmod(_sum + car + res[i+j],10) 
                
                res[i+j] = rem
                res[i+j+1] += car
                
                final_car = car
                car, rem = 0,0
        car = final_car/10
        
        if car :
            res = res + [car]
        
        while res[-1] == 0:
            res.pop()
        return "".join(map(str,res[::-1]))

num1, num2 = "9","0"
print(Solution().multiply(num1,num2))