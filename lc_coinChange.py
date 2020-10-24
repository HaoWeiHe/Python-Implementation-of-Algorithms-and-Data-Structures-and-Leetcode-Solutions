class Solution(object):
    
    def coinChange(self, coins, amount):
   
        table = [[0 for x in range(amount+1)] for y in range(len(coins)+1)] 

        margine = max(coins) +99 

        for i in range(amount+1):
            table[0][i] = margine


        for i in range(1,len(coins)+1):
            for j in range(1,amount + 1):
                coin = coins[i-1]

                if j >= coin:
                    # print("hey",coin,[j-coin])
                    table[i][j] = min(table[i-1][j], table[i][j-coin] +1)
                else:
                    table[i][j] = table[i-1][j]

        return table[-1][-1] if not table[-1][-1] == margine else -1

            
        