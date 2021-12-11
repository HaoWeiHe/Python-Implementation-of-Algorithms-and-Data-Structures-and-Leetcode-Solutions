class Solution:
    """
                    [3,5,2,1,4]
                           v -> far we can go, if reach this far, jump +=1 , update jump_emd
cur_jump_end =       0 3 3 6 6
fargest =            3 6 6 6
ans =                1 1 1 2
    """
    def jump(self, nums):
        ans, cur_jump_end, fargest = 0 , 0, 0
        for idx in range(len(nums) - 1):
            fargest = max(fargest, idx + nums[idx])
            if idx == cur_jump_end:
                ans += 1
                cur_jump_end = fargest
        return ans

    """
          0 1 2 3 4
         [3,5,2,1,4]
            v

            x x x
         while not reach the end of the list:
         jmp ++
         get_next_idx
    determine the next_idx who has the farest jump

    """
    def jump2(self, nums):
        ans, reach_idx = 0, 0
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

        while reach_idx < len(nums) -1: 
            ans += 1
            reach_end, reach_idx = get_next_idx(idx)
            if reach_end:
                return ans 
        return 0
        

nums = [2,3,1,1,4]#[2,1]#,[2,3,0,1,4]
print(Solution().jump(nums))