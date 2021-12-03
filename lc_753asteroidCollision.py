class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        [5,10,-5]
             
        """
        collision = set()
        for idx, ele in enumerate(asteroids):
            if ele < 0:
                tmp_i = idx
                while tmp_i > 0 :
                    tmp_i -= 1
                    if tmp_i in collision:
                        continue
                    if asteroids[tmp_i] < 0 :
                        break
                    if abs(ele) > abs(asteroids[tmp_i]):
                        collision.add(tmp_i)
                    elif abs(ele) == abs(asteroids[tmp_i]):
                        collision.add(idx)
                        collision.add(tmp_i)
                        break
                    else:
                        collision.add(idx)
                        break
              
        return [ele for idx, ele in enumerate(asteroids) if idx not in collision]