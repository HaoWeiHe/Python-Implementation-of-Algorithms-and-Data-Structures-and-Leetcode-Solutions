
class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """

        stack = dict()


        five_coins = 0 
        ten_coins = 0 

        for bill in bills:


            if bill == 5:
                five_coins +=1
            elif bill == 10:
                if five_coins > 0 :
                    five_coins = five_coins - 1
                    ten_coins = ten_coins +1
                else:
                    return False

            elif bill == 20 :
                if five_coins > 0 and ten_coins > 0:
                    five_coins = five_coins -1
                    ten_coins = ten_coins -1
                elif five_coins >=3:
                    five_coins -= 3
                else:
                    return False

        return True