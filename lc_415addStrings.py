class Solution(object):
    def addStrings(self, num1, num2):
        """
        125
       9456
          1 
        """
        if len(num2) > len(num1):
            num2, num1 = num1,num2

        car,res = 0,[]
        for idx in range(len(num1)):
            n1_num = num1[~idx]
            n2_num  = num2[~idx] if len(num2) > idx else 0 
            car,r = divmod(int(n2_num) + int(n1_num) + car,10)
            print(n1_num ,n2_num,car,r)#car,r = 1,7
            res.append(r)#7
        if car:
            res.append(car)
        return "".join(map(str,res[::-1]))

print(Solution().addStrings("98","9"))