class Tree():
    def __init__(self,val,freq):
        self.right = None
        self.left = None
        self.val = val
        self.freq = freq
        self.left_nodes = 0

class Solution(object):
    def countSmaller(self, nums):
        """
        approach 2: use the idea of binary search tree
        input : 5,2,6,1
        rever : 1,6,2,5

        treeNoe : (val, freq_of_val, left_nodes)

        (1,1,0)          ->  res = [0] #the num of right paths
            \
            (6,1,2)      ->  res = [0,1] #the num of right paths, which is freq of root + its' left chidren (1+0)
            /   
          (2,1,0)        ->  res = [0,1,1]
             \
             (5,1,0)      ->  res = [0,1,1,2]

        """
        
        if not nums: return []

        nums.reverse()
        res = []
        root = Tree(nums[0],0)

        for ele in nums:
            counter = 0
            node = root
            while 1 :
                if ele == node.val:
                    counter +=  node.left_nodes #REMEMBER TO ADD LEFTNODE in the end!!
                    node.freq += 1
                    break
                elif ele < node.val:
                    node.left_nodes +=1
                    if node.left:
                        node = node.left
                    else:
                        node.left = Tree(ele,1)
                        break

                elif ele > node.val:
                    counter += node.freq + node.left_nodes
                    if node.right:
                        node = node.right
                    else:
                        node.right = Tree(ele,1)
                        break
            res.append(counter)
        return res[::-1]
         
    def countSmaller2(self, nums):
        """
        approach 1: use the idea of prefix sum #got TLE
        
        input : 5,2,6,1
        
        reverse :1,6,2,5 (reverse to fix in prefix sum)
        
        
        1,2,5,6 (sort 1625)
        0,1,2,3 (index of sort 1625)
        
        1,6,2,5 (rever_of_nums)
        0,3,1,2 ( index of reverse, map)
        
    init     [0,0,0,0] = A
        1 0  [1,0,0,0] -> 0 :A[idx_of_0] +1, and sum(A[idx_of_0-1])
        6 3  [1,0,0,1] -> 1 : A[idx_of_6] +1 and sum()before that indx
        2 1  [1,1,0,1] -> 1: A[idx_of_2] +1 and sum() before that indx
        5 2  [1,1,1,1] -> 2 : A[idx_of_5] +1 and sum() before that indx
        """
        nums.reverse()
        sorted_nums = sorted(nums)
        dic = {val:idx for idx,val in enumerate(sorted_nums)}
        
        indx_of_reverse = [dic[ele] for ele in nums] #0,3,1,2
        init = [0] * (len(nums) + 1)
        res = []
        
        for ele in indx_of_reverse:
            init[ele] += 1
            res.append(sum(init[:ele]))

        return res[::-1]
            
        
        
        