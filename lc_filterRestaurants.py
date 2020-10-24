class Solution(object):
    def filterRestaurants(self, restaurants, veganFriendly, maxPrice, maxDistance):
        """
        :type restaurants: List[List[int]]
        :type veganFriendly: int
        :type maxPrice: int
        :type maxDistance: int
        :rtype: List[int]
        """
       
        scored = collections.defaultdict(list)
        for ele in restaurants:
            _id, rating, vegan,price, distance=ele
         
            if vegan == veganFriendly and price <= maxPrice and distance <= maxDistance:
                score[rating].append(_id)
        
        res = sorted(scored.items(), key = lambda (r,_id): (r, - _id))
        return res