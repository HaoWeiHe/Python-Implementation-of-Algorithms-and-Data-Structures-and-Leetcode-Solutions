"""
      0 1 2 3 4
     [3,5,2,1,4]
        v

        x x x
     while not reach the end of the list:
     jmp = 1
     get_next_idx
determine which is the next_idx (who has the farest jump)

    

"""
class Solution(object):
    def jump(self, nums):
        ans, idx = 0, 0
        def get_next_idx(idx):
            max_jp, next_idx = 0, 0 
            for tmp_idx in range(idx + 1, idx + 1 + nums[idx]):
                if tmp_idx >= len(nums) -1:
                    return True, "_"
                tmp_far = tmp_idx + nums[tmp_idx]
                if tmp_far > max_jp:
                    max_jp = tmp_far
                    next_idx = tmp_idx
            return False, next_idx

        while idx < len(nums) -1:
            
            ans += 1
            reach, idx = get_next_idx(idx)
            if reach:
                return ans

            
        return 0
        

nums = [2,3,1,1,4]#[2,1]#,[2,3,0,1,4]
print(Solution().jump(nums))