class Solution:
    def carPooling(self, trips, capacity):
        """
        (1,2) , (5, -2) (3,3) (7,-3)
        order by tuple[0]
        1:2 ,3:3,  5: -2 , 7:-3
        2      5       3      0
        """
        lst = []
        for c,s,e in trips:
            lst.append((s,c))
            lst.append((e,-c))
        lst.sort()
        cur_num = 0
        for t, c in lst:
            cur_num += c
            if cur_num > capacity:
                return False
        return True
